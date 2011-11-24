# Copyright 2011 Cedric Gaspoz
#
# This file is part of ISannounces. You can download it from:
# http://code.google.com/p/isannounces/
#
# ISannounces is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ISannounces is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ISannounces. If not, see <http://www.gnu.org/licenses/>.

"""Top-level URL mappings for ISannounces."""

# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *

# If you don't want to run Rietveld from the root level, add the
# subdirectory as shown in the following example:
#
#    url(r'subpath/', include('codereview.urls')),
#
urlpatterns = patterns(
    '',
    url(r'', include('mlmgr.urls')),
    )
