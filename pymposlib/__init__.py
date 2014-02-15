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

from .api import get_user_balance


api_calls = {
    'getuserbalance': get_user_balance
}

def get_available_api_calls():
    return[x for x in api_calls.keys()]

def call(action):
    if action not in api_calls:
        return False
    return api_calls[action]()