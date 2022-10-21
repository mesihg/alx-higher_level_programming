#!/usr/bin/python3
""" Make a request and handle HTTPError """
import urllib.request
import sys

if __name__ == '__main__':
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
