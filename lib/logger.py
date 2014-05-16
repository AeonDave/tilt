#!/usr/bin/env python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import logging, sys

logger = logging.getLogger('tiltLogger')
stream = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
stream.setFormatter(formatter)
logger.addHandler(stream)
logger.setLevel(logging.INFO)