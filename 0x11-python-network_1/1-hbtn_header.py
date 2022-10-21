#!/usr/bin/python3
""" Make a request to a URL and displays the value of the X-Request-Id """
import urllib.request
import sys

if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
