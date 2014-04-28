#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/tilt)
See the file 'LICENSE' for copying permission
"""

def sort(value):
    return sorted(value)

def remove_duplicates(value):
    return set(value)

def list_to_string(value):
    data=''
    for host in value:
        if host:
            if type(host) is list:
                for element in host:
                    data += element + " "
            else:
                data += host
            data += " "
    return data
