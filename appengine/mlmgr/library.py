# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Django template library for MLMGR."""

import cgi
import logging

from google.appengine.api import memcache
from google.appengine.api import users

import django.template
import django.utils.safestring
from django.core.urlresolvers import reverse

import models

register = django.template.Library()

user_cache = {}



def get_links_for_users(user_emails):
  """Return a dictionary of email->link to user page and fill caches."""
  link_dict = {}
  remaining_emails = set(user_emails)

  # initialize with email usernames
  for email in remaining_emails:
    nick = email.split('@', 1)[0]
    link_dict[email] = cgi.escape(nick)

  # look in the local cache
  for email in remaining_emails:
    if email in user_cache:
      link_dict[email] = user_cache[email]
  remaining_emails = remaining_emails - set(user_cache)

  if not remaining_emails:
    return link_dict

  # then look in memcache
  memcache_results = memcache.get_multi(remaining_emails,
                                        key_prefix="show_user:")
  for email in memcache_results:
    link_dict[email] = memcache_results[email]
    user_cache[email] = memcache_results[email]
  remaining_emails = remaining_emails - set(memcache_results)

  if not remaining_emails:
    return link_dict

  # and finally hit the datastore
  accounts = models.Account.get_accounts_for_emails(remaining_emails)
  for account in accounts:
    if account and account.user_has_selected_nickname:
      ret = ('<a href="%s" onMouseOver="M_showUserInfoPopup(this)">%s</a>' %
             (reverse('codereview.views.show_user', args=[account.nickname]),
              cgi.escape(account.nickname)))
      link_dict[account.email] = ret

  datastore_results = dict((e, link_dict[e]) for e in remaining_emails)
  memcache.set_multi(datastore_results, 300, key_prefix='show_user:')
  user_cache.update(datastore_results)

  return link_dict


def get_link_for_user(email):
  """Get a link to a user's profile page."""
  links = get_links_for_users([email])
  return links[email]


@register.filter
def show_user(email, arg=None, autoescape=None, memcache_results=None):
  """Render a link to the user's dashboard, with text being the nickname."""
  if isinstance(email, users.User):
    email = email.email()
  if not arg:
    user = users.get_current_user()
    if user is not None and email == user.email():
      return 'me'

  ret = get_link_for_user(email)

  return django.utils.safestring.mark_safe(ret)


@register.filter
def show_users(email_list, arg=None):
  """Render list of links to each user's dashboard."""
  new_email_list = []
  for email in email_list:
    if isinstance(email, users.User):
      email = email.email()
    new_email_list.append(email)

  links = get_links_for_users(new_email_list)

  if not arg:
    user = users.get_current_user()
    if user is not None:
      links[user.email()] = 'me'

  return django.utils.safestring.mark_safe(', '.join(
      links[email] for email in email_list))