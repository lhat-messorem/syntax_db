#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
import sys

#Request class to send and get response from SyntaxDB API url
class Request():
    def __init__(self):
        self.request_url = "https://syntaxdb.com/api/v1"

    def addOptions(self, options):
        #Add options to request url. Format: ?{options}={value}
        self.request_url += '?' + '&'.join([i+'='+options[i] for i in options])

    def addPath(self, path, parameter = None):
        #Add path to request url. Format: /{path}/{parameter}
        if parameter:
            parameter = ''.join([i if re.match('[a-zA-Z0-9_-]', i) else ('%'+i.encode("hex")) for i in parameter])
        self.request_url += ('/'+path) if not parameter else ('/'+path+'/'+parameter)

    def send_request(self):
        try:
            return requests.get(self.request_url).json()
        except:
            print "[!]Unexpected error:", sys.exc_info()[0]
            print "[!]The URL maybe wrong! Please check options and try again!"

    def reset_url(self):
        self.request_url = "https://syntaxdb.com/api/v1"
