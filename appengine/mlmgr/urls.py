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

"""URL mappings for the mlmgr package."""

# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *
import django.views.defaults
from codereview import feeds


urlpatterns = patterns(
    'mlmgr.views',
    (r'^$', 'index'),
    (r'^(\d+)/show$', 'show'),
    (r'^(\d+)/mturk/submit$', 'mturk_submit'),
    (r'^(\d+)/mturk$', 'mturk'),
    (r'^(\d+)/process$', 'process'),
    (r'^update/types$', 'update_types'),
    (r'^update/predictions$', 'accept_predictions'),
    (r'^admin/authorize_prediction/auth_callback$', 'authorize_callback'),
    (r'^admin/authorize_prediction$', 'authorize_prediction'),
    (r'^_ah/xmpp/message/chat/', 'incoming_chat'),
    (r'^_ah/mail/(.*)', 'incoming_mail'),
    (r'^_ah/queue/batchprocess', 'batch_process_messages'),
    (r'^_ah/queue/exportcloudstorage', 'export_cloud_storage'),
    )

feed_dict = {
  'reviews': feeds.ReviewsFeed,
  'closed': feeds.ClosedFeed,
  'mine' : feeds.MineFeed,
  'all': feeds.AllFeed,
  'issue' : feeds.OneIssueFeed,
}

urlpatterns += patterns(
    '',
    (r'^rss/(?P<url>.*)$', 'django.contrib.syndication.views.feed',
     {'feed_dict': feed_dict}),
    )
