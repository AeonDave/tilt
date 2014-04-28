#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import sys, os, core, settings, util

from lib.logger import logger

__version__ = settings.VERSION
__author__ = settings.AUTHOR

def header():
    os.system("clear")
    
    print ""
    print "         ============================================= "
    print "        |  Terminal Ip Lookup Tool v{0}: TILT\t|".format(__version__)
    print "        |  by {0}\t\t\t\t\t|".format(__author__)
    print "         ============================================= "
    print ""

def showhelp():
    print """
    Usage: python tilt.py [Target] [Options] [Output]

    Target:
        -t, --target target       Target URL (e.g. "www.site.com")
    Options:
        -h, --help                Show basic help message
        -v, --version             Show program's version number
        -e, --extensive           Perform extensive ip lookup
        -r, --reverse             Perform e reverse ip lookup
        -g, --google              Perform a search on google
        -u, --update              Update program from repository
    Output: 
        -o, --output file         Print log on a file

    Examples:
        python tilt.py -t google.com -r
        python tilt.py -t 8.8.8.8
        python tilt.py -t google.com -e -o file.log
        python tilt.py -u
    """     

def host_inspect(target):
    
    if core.is_valid_ip(target):
        msg = "[+] Valid ip"
        logger.info(msg)
        msg = "[*] Performing hostname conversion"
        logger.info(msg)
        try:
            value = core.get_host_by_ip(target)
            msg = util.list_to_string(value)
            logger.info(msg)
        except:
            msg = "[-] ERROR: Cannot resolve hostname"
            logger.error(msg)
                
    elif core.is_valid_hostname(target):
        msg = "[+] Valid host"
        logger.info(msg)
        msg = "[*] Performing ip conversion"
        logger.info(msg)
        try:
            value = core.get_host_by_name(target)
            msg = util.list_to_string(value)
            logger.info(msg)
        except:
            msg = "[-] ERROR: Cannot resolve hostname"
            logger.error(msg)
        
    else:
        msg =  "[-] ERROR: You must provide a valid target. Given: "+ target
        showhelp()
        logger.error(msg)
        sys.exit(1) 
        
    
def host_extensive_inspect(target):
    if core.is_valid_ip(target):
        msg = "[+] Valid ip"
        logger.info(msg)
        msg = "[*] Performing hostname conversion"
        logger.info(msg)
        try:
            value = core.get_host_by_ip(target)
            msg = util.list_to_string(value)
            logger.info(msg)
        except:
            msg = "[-] ERROR: Cannot resolve hostname"
            logger.error(msg)
                
    elif core.is_valid_hostname(target):
        msg = "[+] Valid host"
        logger.info(msg)
        msg = "[*] Performing ip conversion"
        logger.info(msg)
        try:
            value = core.get_host_by_name(target)
            msg = util.list_to_string(value)
            logger.info(msg)
        except:
            msg = "[-] ERROR: Cannot resolve hostname"
            logger.error(msg)
    else:
        msg = "[-] ERROR: You must provide a valid target. Given: "+target
        logger.error(msg)
        showhelp()
        sys.exit(1) 

def reverse(target):
    msg = "[*] Performing reverse ip lookup"
    logger.info(msg)
    hosts = core.get_reversed_hosts(target)
    if len(hosts)>0:
        msg = "[+] "+str(len(hosts))+" Domains found"
        logger.info(msg)
        for host in hosts:
            logger.info(host)
    else:
        msg = "[-] No Domains found"
        logger.error(msg)
            
def search(value):
        msg = "[-] Not Implemented Yet"
        logger.error(msg)
