Tilt: Terminal Ip Lookup Tool
====




                                               ████████╗██╗██╗  ████████╗
                                               ╚══██╔══╝██║██║  ╚══██╔══╝
                                                  ██║   ██║██║     ██║   
                                                  ██║   ██║██║     ██║   
                                                  ██║   ██║███████╗██║   
                                                  ╚═╝   ╚═╝╚══════╝╚═╝ 

-------------
 
 Tilt: Terminal ip lookup tool, is a easy and simple tool implemented in Python for ip reconnaissance, with reverse ip lookup.
 
 
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
        
New features will be added in future

Follow the project on: https://github.com/AeonDave/tilt
