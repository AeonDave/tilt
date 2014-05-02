Tilt: Terminal Ip Lookup Tool
====
An automatic ip lookup and reverse probing tool for passive reconnaissance



	████████╗██╗██╗  ████████╗
	╚══██╔══╝██║██║  ╚══██╔══╝
	   ██║   ██║██║     ██║   
	   ██║   ██║██║     ██║   
	   ██║   ██║███████╗██║   
	   ╚═╝   ╚═╝╚══════╝╚═╝   
                          


----

## Description

Tilt: Terminal ip lookup tool, is an easy and simple open source tool implemented in Python for ip/host passive reconnaissance.
It's very handy for first reconnaissance approach and for host data retrieval.

## Features

* Host to IP conversion
* IP to Host conversion
* DNS to IPs
* GeoIP Translation
* Extensive information gathering trough Host-name
	* Whois with:
		* Registrar info
		* Dates
		* Name Server
		* SiteStatus
		* Owner information
		* Additional data
	* Sub domains
		* Percentage of access
	* Extensive Name Server
	* SOA Records
	* DNS Records with extensive data
* Reverse IP Lookup
	* Extensive reverse IP lookup, looking for host with different IP on the same machine
	
## Download and install

You can download the latest version by cloning Tilt from the Git repository:

	git clone https://github.com/AeonDave/tilt.git
	
## Dependencies

With 0.6 version i decided to introduce a library needed to parse html... so you have to install BeautyfulSoup library (http://www.crummy.com/software/BeautifulSoup/).
But don't worry! It's easy!

	pip install beautifulsoup4

or

	easy_install BeautifulSoup4
	
or you just simply download the library and then

	cd BeautifulSoup
	python setup.py install
 
## Usage

    python tilt.py [Target] [Options] [Output]

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
        python tilt.py -t google.com -e -r -o file.log
        python tilt.py -u
        
## Contributing

Feel free to contribute to this project, fork, submit and discuss!

Follow the project on: https://github.com/AeonDave/tilt
