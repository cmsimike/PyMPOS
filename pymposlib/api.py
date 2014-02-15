# pympos - a wrapper for the mpos api
# Copyright (C) 2014  Mike Megally

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from .get_config import get_server, get_api_key
import requests 
import json

URL = 'https://%s/index.php' % get_server()

def _make_request(api_action):
    payload = {
        'page': 'api',
        'action': api_action,
        'api_key': get_api_key(),

    }
    r = requests.get(URL, params=payload)
    return r.text

#getuserbalance
def get_user_balance():
    s = _make_request('getuserbalance')
    return json.loads(s)