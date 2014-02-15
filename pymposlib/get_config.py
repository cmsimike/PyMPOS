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

import ConfigParser
import os 

pymposrc = os.path.expanduser('~/.pymposrc')
config = ConfigParser.ConfigParser()
config.read(pymposrc)


def _config_selection_map(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
        except:
            print 'exception on %s!' % option
            dict1[option] = None
    return dict1

def get_api_key():
    return _config_selection_map('pympos')['apikey']

def get_server():
    return _config_selection_map('pympos')['server']