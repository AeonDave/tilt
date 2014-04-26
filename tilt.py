#!/usr/bin/python

import sys, getopt, socket, re, os, json, urllib2

from subprocess import PIPE
from subprocess import Popen
from settings import GIT_REPOSITORY
from settings import VERSION
from settings import AUTHOR
from settings import ROOTDIR

__version__ = VERSION
__author__ = AUTHOR


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
    Usage: python tilt.py [Target] [Options]

    Target:
        -t target        Target URL (e.g. "www.site.com")
    Options:
        -h, --help                Show basic help message
        -v, --version             Show program's version number
        -r, --reverse             Perform e reverse ip lookup
        -g, --google              Perform a search on google(not working)
        -u, --update              Update program from repository(not working)

    Example:
        python tilt.py -t google.com -r
        python tilt.py -t 8.8.8.8
        python tilt.py -u
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
        print "[-] ERROR: Cannot resolve ip: ", value, err
        sys.exit(1) 

def get_host_by_name(value):
    try:
        host = socket.gethostbyname_ex(value)
        return host
    except socket.gaierror, err:
        print "[-] ERROR: Cannot resolve hostname: ", value, err
        sys.exit(1) 

def get_ip(value):
    try:
        host = socket.gethostbyname(value)
        return host
    except:
        return None

def get_data_from_url(value):
    
    req = urllib2.Request(value)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Connection', 'keep-alive')
    
    try:
        rawdata = json.load(urllib2.urlopen(req))
        return rawdata
    except urllib2.HTTPError, e:
        print e.fp.read()
        sys.exit(2)

def get_reversed_ip_hosts(value):
    
        url = 'http://domains.yougetsignal.com/domains.php?remoteAddress=' + value
        url2 = 'http://reverseip.logontube.com/?url=' + value + '&output=json'
        
        data = get_data_from_url(url)
        data2 = get_data_from_url(url2)
        
        domain = (data['domainArray'])
        domain2 = (data2['response']['domains'])
        
        ip = get_ip(value)
        domains=[]
        
        for site in domain:
            for host in site:
                if host != '':
                    result = get_ip(host)
                    if result==ip or result==None:
                        domains.append(host)
                        
        for site2 in domain2:
            if site2 not in domains:
                result = get_ip(site2)
                if result==ip or result==None:
                    domains.append(site2)
        
        
        
        return sorted(domains)
    
def update():                       
        if not os.path.exists(os.path.join(ROOTDIR, ".git")):
            print "[-] Not a git repository. Please checkout the repository from GitHub (e.g. git clone https://github.com/AeonDave/tilt.git)"
        else:
            print "[*] Updating Tilt from latest version from the GitHub Repository\n" 
            Popen("git reset --hard", shell=True, stdout=PIPE, stderr=PIPE)
            process = Popen("git pull", shell=True, stdout=PIPE, stderr=PIPE)
            Popen("chmod +x ./tilt.py", shell=True, stdout=PIPE, stderr=PIPE)
            process.communicate()
            success = not process.returncode
            if success:
                print "[+] Updated!\n"
            else:
                print "[-] Error!\n"   
           
        sys.exit(0)
        
        
        
# Tilt Startup

try:
    options, args = getopt.getopt(sys.argv[1:], 't:rgvhu', ['target=', 'reverse', 'google', 'version', 'help', 'update'])
except getopt.GetoptError:
    showhelp()
    sys.exit(1)

target=None
reverse=False
google=False

for opt, arg in options:
    if opt in ('-h', '--help'):
        showhelp()
        sys.exit(0)
    elif opt in ('-v', '--version'):
        header()
        sys.exit(0)
    elif opt in ('-u', '--update'):
        header()
        update()
        sys.exit(0)
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
