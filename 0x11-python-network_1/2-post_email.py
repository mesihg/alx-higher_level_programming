#!/usr/bin/python3
""" Make a post request with data """
import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    email_data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email_data).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf8'))
