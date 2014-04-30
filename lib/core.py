#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import socket, re, source, util

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
    domains = source.get_reverse_from_yougetsignal(value, extensive) + source.get_reverse_from_logontube(value, extensive)
    domains = util.remove_duplicates(domains)
    domains = util.sort(domains)
    return domains
