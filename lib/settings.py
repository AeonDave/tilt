#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import os ,sys 

VERSION = "0.5.1 beta"
AUTHOR = "AeonDave"
DESCRIPTION = "Automatic ip lookup and reverse probing tool"
SITE = "https://github.com/AeonDave/tilt.git"
ISSUES_PAGE = ""
GIT_REPOSITORY = "git://github.com/AeonDave/tilt.git"

PLATFORM = os.name
ROOTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
LIBDIR = os.path.abspath(os.path.dirname(__file__))
PYVERSION = sys.version.split()[0]