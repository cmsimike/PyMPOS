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

from setuptools import setup

setup(
    name='PyMPOS',
    version='0.0.1',
    packages=['pymposlib',],
    author='Mike Megally',
    author_email='cmsimike@gmail.com',
    maintainer='Mike Megally',
    maintainer_email='cmsimike@gmail.com',
    license='GPLv2',
    description='PyMPOS - Python wrapper for the MPOS api',
    url='http://github.com/cmsimike/pympos/',
    install_requires=[
        'requests==2.2.1',
    ],
    scripts=['bin/pympos.py'],
)