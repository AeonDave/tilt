#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import sys, getopt, logging

from lib import update
from lib import actions
from lib.logger import logger

        
# Tilt Setup

try:
    options, args = getopt.getopt(sys.argv[1:], 't:rgvhueo:', ['target=', 'reverse', 'google', 'version', 'help', 'update', 'extensive', 'output'])
except getopt.GetoptError:
    actions.showhelp()
    sys.exit(1)

target=None
reverse=False
google=False
extensive=False
output=None

for opt, arg in options:
    if opt in ('-h', '--help'):
        actions.showhelp()
        sys.exit(0)
    elif opt in ('-v', '--version'):
        actions.header()
        sys.exit(0)
    elif opt in ('-u', '--update'):
        actions.header()
        update.update()
        sys.exit(0)
    elif opt in ('-t', '--target'):
        target = arg
    elif opt in ('-r', '--reverse'):
        reverse = True
    elif opt in ('-e', '--extensive'):
        extensive = True
    elif opt in ('-g', '--google'):
        google = True
    elif opt in ('-o', '--output'):
        output = arg
    else:
        actions.header()
        actions.showhelp()
        sys.exit(1)

if not target:
    actions.header()
    actions.showhelp()
    msg = "[-] ERROR: You must provide a target."
    logger.error(msg)
    sys.exit(1) 

if google and reverse:
    msg = "[-] Cannot do reverse ip lookup and google search togheter!"
    logger.error(msg)
    sys.exit(1) 

def main():
    if not output==None:     
        handler = logging.FileHandler(output)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
    logger.info('-----Start-----')
    if not target==None:
        if extensive:
            logger.info('[*]Extensive ip lookup on '+target)
            actions.host_extensive_inspect(target)
        else:
            logger.info('[*]Ip lookup on '+target)
            actions.host_inspect(target)
    if reverse:
        logger.info('[*]Reverse ip lookup on '+target)
        actions.reverse(target)
    if google:
        logger.info('[*]Search on '+target)
        actions.search(target)
    logger.info('-----End-----\n')
# Program

if __name__ == '__main__':
    actions.header()
    main()
    sys.exit(0)
