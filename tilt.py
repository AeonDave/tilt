#!/usr/bin/python

import sys, getopt, socket, re, os, json, urllib2

__version__ = "1.0"
__author__ = "AeonDave"


# Functions Header / Help
def header():
    os.system("clear")
    
    print ""
    print "         =========================================== "
    print "        |  Terminal Ip Lookup Tool v{0}: TILT\t    |".format(__version__)
    print "        |  by {0}\t\t\t\t    |".format(__author__)
    print "         =========================================== "
    print ""

def showhelp():
    print """
    Usage: python tilt.py [Target] [options]

    Target:
        -t target        Target URL (e.g. "www.site.com")
    Options:
        -h, --help        Show basic help message
        -v, --version        Show program's version number
        -r            Perform e reverse ip lookup
        -g            Perform a search on google(not working)

    Example:
        python tilt.py -t google.com
        python tilt.py -t 8.8.8.8
    """
    
# Functions

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
    except socket.gaierror, err:
        return "[-] ERROR: Cannot resolve ip: ", value, err

def get_host_by_name(value):
    try:
        host = socket.gethostbyname_ex(value)
        return host
    except socket.gaierror, err:
        return "[-] ERROR: Cannot resolve hostname: ", value, err

def get_ip(value):
    try:
        host = socket.gethostbyname(value)
        return host
    except:
        return None


def get_reversed_ip_hosts(value):
        url = 'http://domains.yougetsignal.com/domains.php?remoteAddress=' + value
        req = urllib2.Request(url)
        req.add_header('Referer', 'http://www.yougetsignal.com/tools/web-sites-on-web-server/')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Connection', 'keep-alive')
        try:
            rawdata = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            return e.fp.read()
        data = json.load(rawdata)
        domain = (data['domainArray'])
        ip = (data['remoteIpAddress'])
        domains=[]
        for site in domain:
            for host in site:
                if host != '':
                    result= get_ip(host)
                    if result==ip or result==None:
                        domains.append(host)
        return domains

                        
         
# Tilt Startup

try:
    options, args = getopt.getopt(sys.argv[1:], 't:rgvh', ['target=', 'reverse', 'google', 'version', 'help'])
except getopt.GetoptError:
    showhelp()
    sys.exit(1)

target=None
reverse=False
google=False

for opt, arg in options:
    if opt in ('-h', '--help'):
        showhelp()
        sys.exit(2)
    elif opt in ('-v', '--version'):
        header()
        sys.exit(2)
    elif opt in ('-t', '--target'):
        target = arg
    elif opt in ('-r', '--reverse'):
        reverse = True
    elif opt in ('-g', '--google'):
        google = True
    else:
        header()
        showhelp()
        sys.exit(1)

if not target:
    header()
    showhelp()
    print "[-] ERROR: You must provide a target.\n"
    sys.exit(1) 


# Program

if __name__ == '__main__':
    header()

if is_valid_ip(target):
    print "[+] Valid ip"
    print "[*] Performing hostname conversion \n"
    try:
        print get_host_by_ip(target), "\n"
    except:
        print "[-] ERROR: Cannot resolve hostname"
        
elif is_valid_hostname(target):
    print "[+] Valid host"
    print "[*] Performing ip conversion \n"
    print get_host_by_name(target), "\n"
    
else:
    print "[-] ERROR: You must provide a valid target. Given: ", target
    showhelp()
    sys.exit(1) 

if reverse:
    print "[*] Performing reverse ip lookup \n"
    hosts = get_reversed_ip_hosts(target)
    if len(hosts)>0:
        print "[+] "+str(len(hosts))+" Domains found \n"
        for host in hosts:
            print host
    else:
        print "[-] No Domains found \n"
sys.exit(0) 
