#!/usr/bin/env python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import sys, core
from lib.logger import logger
from bs4 import BeautifulSoup

def get_reverse_from_yougetsignal(value, extensive):
    url = 'http://domains.yougetsignal.com/domains.php?remoteAddress=' + value
    data = core.get_json_from_url(url)
    status = (data['status'])
    domains=[]
    if status=='Success':
        domain = (data['domainArray'])
        if not core.get_ip(value) == False:
            
            ip = core.get_ip(value)
            
            for value in domain:
                for site in value:
                    if site != '':
                        if not extensive:
                            result = core.get_ip(site)
                            if result==ip or result==None:
                                domains.append(site)
                        elif extensive:
                            result = core.get_ip(site)
                            domains.append(site + " " + result)
        return domains
    else:
        return False
    
def get_reverse_from_logontube(value, extensive):  
    url = 'http://reverseip.logontube.com/?url=' + value + '&output=json'
    data = core.get_json_from_url(url)
    domain = (data['response']['domains'])
    domains=[]
    if not core.get_ip(value) == False:
        ip = core.get_ip(value)
        for site in domain:
            if site != '':
                if not extensive:
                    result = core.get_ip(site)
                    if result==ip or result==None:
                        domains.append(site)
                elif extensive:
                    result = core.get_ip(site)
                    domains.append(site + " " + result)
    return domains

def get_from_who_is(value, type):
    
    whois='http://who.is/whois/'
    info='http://who.is/website-information/'
    dns='http://who.is/dns/'
    
    if type == 0:
        url=whois
    if type == 1:
        url=info
    if type == 2:
        url=dns
        
    rawdata = core.get_html_from_url(url+value)
    if rawdata:
        parser = BeautifulSoup(rawdata)
        blocks = parser.find_all('div','domain-data')
        for block in blocks:
            title = block.header.h5.get_text()
            table = block.table
            if table:
                logger.info('-----'+title.strip()+'-----')
                rows = table.find_all('tr')
                for row in rows:
                    descriptions = row.find_all('th')
                    datas = row.find_all('td')
                    value=''
                    for description in descriptions:
                        if description.get_text().strip():
                            value = value + '-' + description.get_text().strip() 
                    if value:
                        logger.info(value)
                    value=''
                    for data in datas:
                        if data.get_text().strip():
                            value = value + ' ' + data.get_text().strip()
                    if value:
                        logger.info(value) 
    else:
        logger.error('[-] Error: Invalid host given for extensive data')
