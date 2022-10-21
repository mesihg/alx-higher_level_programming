#!/usr/bin/python3
""" Make a post request with data """
import urllib.parse
import urllib.request
import sys

email_data = {'email': sys.argv[2]}
data = urllib.parse.urlencode(email_data).encode('ascii')
request = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(request) as resp:
    print(resp.read().decode('utf8'))
