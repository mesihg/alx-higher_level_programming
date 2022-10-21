#!/usr/bin/python3
""" "Make a request and display errors if any"""
import requests
import sys

if __name__ == '__main__':
    resp_data = requests.get(sys.argv[1])
    if resp_data.status_code >= 400:
        print("Error code: {}".format(resp_data.status_code))
    else:
        print(resp_data.text)
