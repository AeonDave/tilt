#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import sys, os, core, settings, util

from lib.logger import logger
from lib.settings import GEOIPFILE

__version__ = settings.VERSION
__author__ = settings.AUTHOR

def header():
    os.system("clear")
    
    print ""
    print "         =============================================== "
    print "        |  Terminal Ip Lookup Tool v{0}: TILT\t|".format(__version__)
    print "        |  by {0}\t\t\t\t\t|".format(__author__)
    print "         =============================================== "
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

def host_inspect(target, extensive):
    
    if core.is_valid_ip(target):
        msg = "Ip Validation OK"
        logger.debug(msg)
        msg = "[+] Valid ip"
        logger.info(msg)
        msg = "[*] Performing hostname conversion"
        logger.info(msg)
        try:
            value = core.get_host_by_ip(target)
            util.list_to_string(value)
        except:
            msg = "[-] ERROR: Cannot resolve hostname"
            logger.error(msg)
                
    elif core.is_valid_hostname(target):
        msg = "Host Validation OK"
        logger.debug(msg)
        msg = "[+] Valid host"
        logger.info(msg)
        msg = "[*] Performing ip conversion"
        logger.info(msg)
        try:
            value = core.get_host_by_name(target)
            util.list_to_string(value)
        except:
            msg = "[-] ERROR: Cannot resolve hostname"
            logger.error(msg)
            
    else:
        msg =  "[-] ERROR: You must provide a valid target. Given: "+ target
        showhelp()
        logger.error(msg)
        sys.exit(1)
    
    db = GEOIPFILE
    geo = core.ip_to_country(core.get_ip(target), db)
    if geo:
        msg = "[+] The host is situated in "+geo
        logger.info(msg)
    else:
        msg = "[-] Cannot geolocalize the host"
        logger.warning(msg)
    
    if extensive:
        msg = "Extensive probing"
        logger.debug(msg)
        
        msg = "[*] Starting extensive information gathering"
        logger.info(msg)

        whois = core.get_extensive_data(target, 0)

        info = core.get_extensive_data(target, 1)

        dns = core.get_extensive_data(target, 2)


def reverse(target, extensive):
    msg = "Reverse probing"
    logger.debug(msg)
    hosts = core.get_reversed_hosts(target, extensive)
    if len(hosts)>0:
        if len(hosts)==1:
            msg = "[+] "+str(len(hosts))+" Domain found"
            logger.info(msg)
            for host in hosts:
                logger.info(host)
        else:
            msg = "[+] "+str(len(hosts))+" Domains found"
            logger.info(msg)
            for host in hosts:
                logger.info(host)
    else:
        msg = "[-] No Domains found"
        logger.error(msg)
            
        
def search(value):
    msg = "Search probing"
    logger.debug(msg)
    msg = "[-] Not Implemented Yet"
    logger.error(msg)
