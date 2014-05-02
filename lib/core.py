#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import socket, re, json, urllib2, source, util, geoip
from lib.logger import logger

def is_valid_ip(ip):
    is_valid = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)
    if is_valid:
        return True
    else:
        return False

def is_valid_hostname(hostname):
    is_valid = re.match("^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$", hostname)
    if is_valid:
        return True
    else:
        return False

def get_host_by_ip(value):
    try:
        ip = socket.gethostbyaddr(value)
        return ip
    except:
        return False

def get_host_by_name(value):
    try:
        host = socket.gethostbyname_ex(value)
        return host
    except:
        return False 

def get_ip(value):
    try:
        host = socket.gethostbyname(value)
        return host
    except:
        return False
    
def get_reversed_hosts(value, extensive):
    
    source1 = source.get_reverse_from_yougetsignal(value, extensive)
    source2 = source.get_reverse_from_logontube(value, extensive)
    
    domains=[]
    error=False
    if source1:
        domains = domains + source1
    else:
        error=True
    if source2:
        domains = domains + source2
    else:
        error=True
    if error:
        logger.warning('[*] One source responded badly: Reverse ip lookup may be inaccurate')
    domains = util.remove_duplicates(domains)
    domains = util.sort(domains)
    return domains

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

def get_html_from_url(value):
    
    req = urllib2.Request(value)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Connection', 'keep-alive')
    
    try:
        rawdata = urllib2.urlopen(req)
        return rawdata.read()
    except urllib2.HTTPError, e:
        msg = e.fp.read() 
        logger.error(msg)
        sys.exit(2)

def ip_to_country(value, db):
    return geoip.country(value, db)

def get_extensive_data(value, type):
    data = source.get_from_who_is(value, type)
    return data
