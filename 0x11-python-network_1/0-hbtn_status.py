#!/usr/bin/python3
""" Fetch data using urllib """
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        resp_data = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(resp_data)))
        print("\t- content: {}".format(resp_data))
        print("\t- utf8 content: {}".format(resp_data.decode('utf8')))
