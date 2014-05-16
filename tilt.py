#!/usr/bin/env python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import sys, getopt, logging

from lib import update
from lib import actions
from lib.logger import logger
from lib.settings import GEOIPFILE  
# Tilt Setup

try:
    options, args = getopt.getopt(sys.argv[1:], 't:ragvhueo:', ['target=', 'reverse', 'google', 'version', 'help', 'update', 'extensive', 'output'])
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
    if output:     
        handler = logging.FileHandler(output)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
    logger.info('-----Start-----')
    
    if target:
        if extensive:
            logger.info('[*] Starting extensive ip lookup on '+target)
        else:
            logger.info('[*] Starting ip lookup on '+target)
        actions.host_inspect(target, extensive)
        logger.info('[*] Ip Lookup completed')
        
    if reverse and not extensive:
        logger.info('[*] Starting reverse ip lookup on '+target)
        actions.reverse(target, False)
        logger.info('[*] Reverse ip lookup completed')
        
    if reverse and extensive:
        logger.info('[*] Starting Extensive reverse ip lookup on '+target)
        logger.warning('[*] This feature shows all domains pointing on same server but with different ip')
        actions.reverse(target, True)
        logger.info('[*] Extensive reverse ip lookup completed')
        
    if google:
        logger.info('[*] Starting search on '+target)
        actions.search(target)
        logger.info('[*] Search completed')
        
    if output: 
        logger.info('[+] File log written: ' + output)
    logger.info('-----End-----\n')
# Program

if __name__ == '__main__':
    actions.header()
    main()
    sys.exit(0)
