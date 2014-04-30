#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

import sys, os
from lib.logger import logger
from subprocess import PIPE
from subprocess import Popen
from settings import ROOTDIR

def update():
    if not os.path.exists(os.path.join(ROOTDIR, ".git")):
        msg = "[-] Not a git repository. Please checkout the repository from GitHub (e.g. git clone https://github.com/AeonDave/tilt.git)"
        logger.error(msg)
    else:
        msg = "[*] Updating Tilt from latest version from the GitHub Repository\n" 
        logger.info(msg)
        Popen("git stash", shell=True, stdout=PIPE, stderr=PIPE)
        Popen("git stash drop", shell=True, stdout=PIPE, stderr=PIPE)
        process = Popen("git pull origin master", shell=True, stdout=PIPE, stderr=PIPE)
        process.communicate()
        success = not process.returncode
                
        if success:
            msg = "[+] Updated!\n"
            logger.info(msg)
            sys.exit(0)
        else:
            msg = "[-] Error!\n" 
            logger.error(msg)
            sys.exit(1)  
