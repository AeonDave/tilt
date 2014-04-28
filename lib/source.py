#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import sys, json, urllib2, core
from lib.logger import logger

def get_json_from_url(value):
    
    req = urllib2.Request(value)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Connection', 'keep-alive')
    
    try:
        rawdata = json.load(urllib2.urlopen(req))
        return rawdata
    except urllib2.HTTPError, e:
        msg = e.fp.read() 
        logger.error(msg)
        sys.exit(2)

def get_reverse_from_yougetsignal(value):
    url = 'http://domains.yougetsignal.com/domains.php?remoteAddress=' + value
    data = get_json_from_url(url)
    domain = (data['domainArray'])
    if not core.get_ip(value) == False:
        
        ip = core.get_ip(value)
        domains=[]
            
        for value in domain:
            for site in value:
                if site != '':
                    result = core.get_ip(site)
                    if result==ip or result==None:
                        domains.append(site)
        return domains
    else:
        return False
    
def get_reverse_from_logontube(value):  
    url = 'http://reverseip.logontube.com/?url=' + value + '&output=json'
    data = get_json_from_url(url)
    domain = (data['response']['domains'])
    if not core.get_ip(value) == False:
        ip = core.get_ip(value)
        
        domains=[]
    
        for site in domain:
            if site != '':
                result = core.get_ip(site)
                if result==ip or result==None:
                    domains.append(site)  
        return domains
    else:
        return False
    
                
                
                
