# Copyright 2011 Cedric Gaspoz
#
# This file is part of ISannounces. You can download it from:
# http://code.google.com/p/isannounces/
#
# ISannounces is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# ISannounces is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ISannounces. If not, see <http://www.gnu.org/licenses/>.

"""Views for mlmgr"""


### Imports ###
from __future__ import with_statement
import pickle
from google.appengine.api import files

# Python imports
import binascii
import datetime
import email  # see incoming_mail()
import email.utils
import logging
import md5
import os
import random
import re
import urllib
from cStringIO import StringIO
from xml.etree import ElementTree
import httplib2

# AppEngine imports
from django.contrib import messages
from google.appengine.api import mail
from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.api import urlfetch
from google.appengine.api import xmpp
from google.appengine.api.app_identity.app_identity import get_service_account_name
from google.appengine.ext import db
from google.appengine.ext.db import djangoforms
from google.appengine.ext.webapp import xmpp_handlers
from google.appengine.runtime import DeadlineExceededError
from google.appengine.runtime import apiproxy_errors
from google.appengine.api import taskqueue

# OAuth imports
from oauth2client.appengine import StorageByKeyName
from oauth2client.client import OAuth2WebServerFlow

# Django imports
# TODO(guido): Don't import classes/functions directly.
from django import forms
# Import settings as django_settings to avoid name conflict with settings().
from django.conf import settings as django_settings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response
import django.template
from django.template import RequestContext
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

# Local imports
import unicodedata
from codereview import library, engine
import models
import google_prediction


### Constants ###


IS_DEV = os.environ['SERVER_SOFTWARE'].startswith('Dev')  # Development server


### Form classes ###

class MailingListForm(djangoforms.ModelForm):

  class Meta:
    model = models.MailingList
    exclude = ['created', 'modified']


### Exceptions ###


class InvalidIncomingEmailError(Exception):
  """Exception raised by incoming mail handler when a problem occurs."""


### Helper functions ###


### Queues ###

def batch_process_messages(request):
    messages = models.Message.all()
    for message in messages:
        _process_message(message)
    return HttpResponse()

def export_cloud_storage(request):
    try:
        files.gs
    except AttributeError:
        import gs
        files.gs = gs
    # Create a file
    filename = '/gs/isannounces/isan-ml-training.txt'
    writable_file_name = files.gs.create(filename, mime_type='text/plain', acl='project-private')

    messages = models.Message.all()

    # Open and write the file.
    with files.open(writable_file_name, 'a') as f:
        for message in messages:
            f.write('"%s", "%s %s"\n' % (message.type, message.processed_subject, message.processed_body))

    # Finalize the file.
    files.finalize(writable_file_name)
    logging.info('The messages where successfully exported to Google Cloud Storage under filename: %s' % (filename,))
    return HttpResponse()

# Counter displayed (by respond()) below) on every page showing how
# many requests the current incarnation has handled, not counting
# redirects.  Rendered by templates/base.html.
counter = 0


def respond(request, template, params=None):
  """Helper to render a response, passing standard stuff to the response.

  Args:
    request: The request object.
    template: The template name; '.html' is appended automatically.
    params: A dict giving the template parameters; modified in-place.

  Returns:
    Whatever render_to_response(template, params) returns.

  Raises:
    Whatever render_to_response(template, params) raises.
  """
  global counter
  counter += 1
  if params is None:
    params = {}
  must_choose_nickname = False
  uploadpy_hint = False
  if request.user is not None:
    account = models.Account.current_user_account
    #must_choose_nickname = not account.user_has_selected_nickname()
    #uploadpy_hint = account.uploadpy_hint
  params['request'] = request
  params['counter'] = counter
  params['user'] = request.user
  params['is_admin'] = request.user_is_admin
  params['is_dev'] = IS_DEV
  params['media_url'] = django_settings.MEDIA_URL
  full_path = request.get_full_path().encode('utf-8')
  if request.user is None:
    params['sign_in'] = users.create_login_url(full_path)
  else:
    params['sign_out'] = users.create_logout_url(full_path)
    account = models.Account.current_user_account
    if account is not None:
      params['xsrf_token'] = account.get_xsrf_token()
  params['must_choose_nickname'] = must_choose_nickname
  params['uploadpy_hint'] = uploadpy_hint
  params['isannounces_revision'] = django_settings.ISANNOUNCES_REVISION
  try:
    return render_to_response(template, params,
                              context_instance=RequestContext(request))
  except DeadlineExceededError:
    logging.exception('DeadlineExceededError')
    return HttpResponse('DeadlineExceededError', status=503)
  except apiproxy_errors.CapabilityDisabledError, err:
    logging.exception('CapabilityDisabledError: %s', err)
    return HttpResponse('Rietveld: App Engine is undergoing maintenance. '
                        'Please try again in a while. ' + str(err),
                        status=503)
  except MemoryError:
    logging.exception('MemoryError')
    return HttpResponse('MemoryError', status=503)
  except AssertionError:
    logging.exception('AssertionError')
    return HttpResponse('AssertionError')
  finally:
    library.user_cache.clear() # don't want this sticking around


### Decorators for request handlers ###


def post_required(func):
  """Decorator that returns an error unless request.method == 'POST'."""

  def post_wrapper(request, *args, **kwds):
    if request.method != 'POST':
      return HttpResponse('This requires a POST request.', status=405)
    return func(request, *args, **kwds)

  return post_wrapper

def message_required(func):
  """Decorator that processes the message_id handler argument."""

  def message_wrapper(request, message_id, *args, **kwds):
    message = models.Message.get_by_id(int(message_id))
    if message is None:
      return HttpResponseNotFound('No message exists with that id (%s)' %
                                  message_id)
#    if issue.private:
#      if request.user is None:
#        return HttpResponseRedirect(
#            users.create_login_url(request.get_full_path().encode('utf-8')))
#      if not _can_view_issue(request.user, issue):
#        return HttpResponseForbidden('You do not have permission to '
#                                     'view this issue')
    request.message = message
    return func(request, *args, **kwds)

  return message_wrapper

### Request handlers ###


def index(request):
  """/ - Show a list of patches."""
  if request.user is None:
    return all(request)
  else:
    return all(request)

@message_required
def show(request):
    """/<message>/show - Show a <message>"""
    message = request.message
    return respond(request, 'message.html',
            {'message': message,
             'types': models.TYPE_CHOICES,})

@message_required
def print_message(request):
    """/<message>/print - Print a <message>"""
    message = request.message
    return respond(request, 'message_print.html',
            {'message': message,
            })

@message_required
def mturk(request):
    """/<message>/mturk - Start a HIT on a <message>"""
    message = request.message
    mturk = {
        'hit_id': request.GET.get('hitId') or '',
        'assignment_id': request.GET.get('assignmentId') or '',
    }

    if mturk['assignment_id']=='ASSIGNMENT_ID_NOT_AVAILABLE':
        # We should prevent the registration of the attempt
        pass
    return respond(request, 'mturk.html',
            {'message': message,
             'mturk': mturk,
             'types': models.TYPE_CHOICES,})

@message_required
def mturk_submit(request):
    """/<message>/mturk/submit - Submit a HIT on a <message>"""
    message = request.message

    form = request.POST
    assignment_id = form['assignment_id']
    hit_id = form['hit_id']
    comments = form['comments']

    #message_ids = []
    #for id in request.POST.getlist('messageID'):
    #    message_ids.append(int(id))

    hit = models.MturkHIT()
    hit.assignment_id = assignment_id
    hit.hit_id = hit_id
    hit.comments = comments
    hit.message = message
    
    return HttpResponseRedirect('https://workersandbox.mturk.com/mturk/externalSubmit?assignmentId=%s&message_id=%s&type=%s' % (assignment_id, message.key().id(), message.type))

@message_required
def process(request):
    """/<message>/preprocess - Preprocess a <message> for prediction"""
    message = request.message
    message = _process_message(message)
    taskqueue.add(queue_name='ispeech', params={'word_key': new_word.key()})
    return HttpResponseRedirect(reverse(show, args=[message.key().id()]))

def _process_message(message):
    """This do the job of pre-processing a message for the Google Prediction API"""
    body = message.body
    subject = message.subject

    try:
        decoded_subject = email.header.decode_header(subject)
        if decoded_subject[0][1]:
            message.subject = decoded_subject[0][0].decode(decoded_subject[0][1])
    except:
        logging.error('Unable to decode subject: %r', subject)

    # We process the body and the subject
    message.processed_body = _process_string(body)
    message.processed_subject = _process_string(subject)

    # We store the message
    message.put()

    return message

def _process_string(input_string):
    """This do the job of pre-processing a message for the Google Prediction API"""

    #1 We should remove all accented characters
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_string))
    output_string = u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

    #2 We should remove all non alphanumerical characters
    # Hint, \w match alphanumeric characters AND underscores
    output_string = re.sub(r'[^\w]', ' ', output_string)
    output_string = output_string.replace('_', ' ')

    #3 We should remove all multiple spaces
    output_string = ' '.join(output_string.split())

    #4 We should have everything lower case
    output_string = output_string.lower()

    #5 All done, we return the string
    return output_string

@post_required
def update_types(request):
    form = request.POST
    type = form['type']
    message_ids = []
    for id in request.POST.getlist('messageID'):
        message_ids.append(int(id))
    logging.info('We will update messages: %s with type: %s' % (message_ids, type))
    for message_id in message_ids:
        message = models.Message.get_by_id(int(message_id))
        message.type = type
        message.put()
    messages.info(request, 'The following messages: %s were updated with type: %s' % (message_ids, type))
    return HttpResponseRedirect(reverse(index))

@post_required
def accept_predictions(request):
    message_ids = []
    for id in request.POST.getlist('messageID'):
        message_ids.append(int(id))
    #logging.info('We will update messages: %s with type: %s' % (message_ids, type))
    for message_id in message_ids:
        message = models.Message.get_by_id(int(message_id))
        message.type = message.prediction
        message.put()
        logging.info('Prediction accepted for message: %s -> type: %s' % (message_ids, message.type))
    #messages.info(request, 'The following messages: %s were updated with type: %s' % (message_ids, type))
    return HttpResponseRedirect(reverse(index))

def all(request):
    """/all[?show=<positions|conferences|journals|books|others>]

    Show a list of up to DEFAULT_LIMIT recent messages. Messages can be filtered based on the value of show.
    """

    show = request.GET.get('show') or ''
    logging.info('A filter on: "%s" was requested.' % show)

    if show in ['NA','positions', 'conferences', 'journals', 'books', 'others']:
        if show == 'NA':
            #Not the best way to achieve our goal, but it's enough
            show= 'NAA'
        logging.info('Show in list')
        messages = models.Message.all()
        messages.filter("type = ", show[:-1])
        messages.order("-created")
        if show == 'NAA':
            #Not the best way to achieve our goal, but it's enough
            show= 'unsorted'
    else:
        show= ''
        logging.info('Show NOT in list')
        messages = models.Message.all()
        messages.order("-created")
    return respond(request, 'all_messages.html',
            {'messages_list': messages,
             'types': models.TYPE_CHOICES,
             'show': show})
#  return _paginate_issues(reverse(all),
#                          request,
#                          query,
#                          'mlmgr.html',
#                          extra_nav_parameters=nav_parameters,
#                          extra_template_params=dict(closed=closed))

DEFAULT_MSG = ("Thanks for asking! But I'm so sorry not being able to understand your message...\n"
               "Currently I can only understand /show, /set, /spam and /help commands.")
NO_ID_MSG = ("Oups, you submitted the wrong message ID: %s. This ID does not correspond to any message in my system.")
HELP_MSG = ("You can use the following commands: /show, /set, /spam and /help.\n"
            "/show <ID> display the body of the message <ID>\n"
            "/ok <ID> set the prediction as type for the message <ID>\n"
            "/set <ID> <TYPE> set the type of the message <ID> to %s\n"
            "/spam <ID> tag the message <ID> as a spam.")
TYPES_DICT = {1: 'conference', 2: 'journal', 3: 'book', 4: 'position', 5: 'other', 6: 'NA'}

@post_required
def incoming_chat(request):
    """/_ah/xmpp/message/chat/

    This handles incoming XMPP (chat) messages.

    Just reply saying we ignored the chat.
    """
    try:
        msg = xmpp.Message(request.POST)
    except xmpp.InvalidMessageError, err:
        logging.warn('Incoming invalid chat message: %s' % err)
        return HttpResponse('')
    if msg.body[0]=='/':
        # There is a command in the message
        xmpp_body = msg.body[1:].split()
        if xmpp_body[0] in ['show', 'set', 'ok', 'spam', 'help']:
            # We received a valid command
            xmpp_command = xmpp_body[0]
            xmpp_args = xmpp_body[1:]
            if xmpp_command=='show' and len(xmpp_args)==1:
                message = models.Message.get_by_id(int(xmpp_args[0]))
                if message:
                    sts = msg.reply("%s\n%s" % (message.subject, message.body))
                else:
                    sts = msg.reply(NO_ID_MSG % (int(xmpp_args[0]),))
            elif xmpp_command=='set' and len(xmpp_args)==2:
                message = models.Message.get_by_id(int(xmpp_args[0]))
                if int(xmpp_args[1]) in TYPES_DICT and message:
                    message.type = TYPES_DICT[int(xmpp_args[1])]
                    message.put()
                    sts = msg.reply("Message: '%s' set to type: '%s'. Thank you!" % (message.subject, TYPES_DICT[int(xmpp_args[1])]))
                else:
                    sts = msg.reply(NO_ID_MSG % (int(xmpp_args[0]),))
            elif xmpp_command=='spam' and len(xmpp_args)==1:
                message = models.Message.get_by_id(int(xmpp_args[0]))
                if message:
                    message.spam = True
                    message.put()
                    sts = msg.reply("Message: '%s' tagged as SPAM. Thank you!" % (message.subject,))
                else:
                    sts = msg.reply(NO_ID_MSG % (int(xmpp_args[0]),))
            elif xmpp_command=='ok' and len(xmpp_args)==1:
                message = models.Message.get_by_id(int(xmpp_args[0]))
                if message:
                    message.type = message.prediction
                    message.put()
                    sts = msg.reply("Message: '%s' set to type: '%s'. Thank you!" % (message.subject, message.prediction))
                else:
                    sts = msg.reply(NO_ID_MSG % (int(xmpp_args[0]),))
            elif xmpp_command=='help':
                sts = msg.reply(HELP_MSG % (TYPES_DICT,))
            else:
                sts = msg.reply(DEFAULT_MSG)
        else:
            # This is an invalid command, we send back a generic message
            sts = msg.reply(DEFAULT_MSG)
    else:
        # There is no command in the message, we send back a generic message
        sts = msg.reply(DEFAULT_MSG)
    logging.debug('XMPP status %r', sts)
    return HttpResponse('')


@post_required
def incoming_mail(request, recipients):
  """/_ah/mail/(.*)

  Handle incoming mail messages.

  The issue is not modified. No reviewers or CC's will be added or removed.
  """
  try:
    _process_incoming_mail(request.raw_post_data, recipients, request.path)
  except InvalidIncomingEmailError, err:
    logging.debug(str(err))
  return HttpResponse('')


def _process_incoming_mail(raw_message, recipients, mailing_list):
    """Process an incoming email message."""
    recipients = [x[1] for x in email.utils.getaddresses([recipients])]

    incoming_msg = mail.InboundEmailMessage(raw_message)

    mailing_list_acronym = mailing_list.split('/')[3].split('@')[0]

    query = models.MailingList.all().filter('acronym =', mailing_list_acronym.lower())
    mailing_list = query.get()
    if mailing_list is None:
        # Create a new mailing-list
        newml = models.MailingList(name=mailing_list_acronym,
                                   acronym=mailing_list_acronym.lower())
        newml.put()
        mailing_list = newml
    else:
        mailing_list.clean_subject='[AISWorld] '
        mailing_list.put()

    logging.info("Received a message from: " + incoming_msg.sender + " TO: " + str(recipients) + " for ML " + mailing_list_acronym)

    if 'X-Google-Appengine-App-Id' in incoming_msg.original:
        raise InvalidIncomingEmailError('Mail sent by App Engine')

    subject = incoming_msg.subject or ''
    sender = email.utils.parseaddr(incoming_msg.sender)[1]
    original = str(incoming_msg.original)

    body = None
    for content_type, payload in incoming_msg.bodies('text/plain'):
        body = payload.decode()
        break
    if body is None or not body.strip():
        raise InvalidIncomingEmailError('Ignoring empty message.')

    # We need to check if the header is internationalized
    try:
        decoded_subject = email.header.decode_header(subject)
        if decoded_subject[0][1]:
            subject = decoded_subject[0][0].decode(decoded_subject[0][1])
    except:
        logging.error('Unable to decode subject: %r', subject)

    # If the subject is long, this might come wrapped into more than one line.
    subject = ' '.join([x.strip() for x in subject.splitlines()])
    subject = subject.replace(mailing_list.clean_subject, '')
    query = models.MailingList.all()
    mailing_list = query.get()

    processed_subject = _process_string(subject)
    processed_body = _process_string(body)

    email_date = email.utils.parsedate_tz(incoming_msg.date)

    msg = models.Message(mailing_list = mailing_list,
                         subject=subject,
                         processed_body = processed_body,
                         processed_subject = processed_subject,
                         sender=db.Email(sender),
                         original=db.Text(original),
                         body=db.Text(body),
                         spam=False)
    if email_date:
        msg.created = datetime.datetime(*email_date[:6])-datetime.timedelta(seconds= email_date[-1])

    # We now predict the type with Google Predict API
    credentials = StorageByKeyName(models.Credentials, "key_for_prediction_credentials", 'credentials').get()
    logging.info('CREDENTIALS: ' + str(credentials))
    model = django_settings.GOOGLE_PREDICTION_MODEL
    if credentials:
        # Make the Google Prediction API call
        query = '"'+processed_subject+' '+processed_body+'"'
        [prediction, scores] = google_prediction.Predict(credentials, model, query)
        msg.prediction = prediction
        msg.scores = scores
    msg.put()

    user_address = 'cedric.gaspoz@gmail.com'
    chat_message_sent = False
    msg = "Message '%s' from: %s\nPrediction: %s\n%s" % (msg.key().id(), incoming_msg.sender, msg.prediction, msg.subject)
    status_code = xmpp.send_message(user_address, msg)
    chat_message_sent = (status_code == xmpp.NO_ERROR)

    if not chat_message_sent:
        logging.error("Unable to send XMPP message: %s" % msg)


def authorize_prediction(request):
    user = users.get_current_user()
    # If we don't find OAuth 2.0 credentials for the user in the datastore, then we need to go through
    # the Web Server Flow to acquire those credentials.
    flow = OAuth2WebServerFlow(
        # Visit https://code.google.com/apis/console to
        # generate your client_id, client_secret and to
        # register your redirect_uri.
        client_id=django_settings.OAUTH_CLIENT_ID,
        client_secret=django_settings.OAUTH_CLIENT_SECRET,
        scope='https://www.googleapis.com/auth/prediction',
        user_agent='isannounces/1.0')

    authorize_url = flow.step1_get_authorize_url(request.build_absolute_uri(reverse(authorize_callback)))
    # The flow uses the information provided to give you the URL to redirect the user to, so they can grant
    # the web application access.
    memcache.set(user.user_id(), pickle.dumps(flow))
    return HttpResponseRedirect(authorize_url)

def authorize_callback(request):
    user = users.get_current_user()
    flow = pickle.loads(memcache.get(user.user_id()))
    if flow:
        code = request.GET.get('code')
        credentials = flow.step2_exchange(code)
        StorageByKeyName(models.Credentials, "key_for_prediction_credentials", 'credentials').put(credentials)
        return HttpResponseRedirect(reverse(index))
    else:
        pass