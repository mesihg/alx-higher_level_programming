#!/usr/bin/python3
""" Fetch data using request and displays the value of X-Request-Id """
import requests
import sys

if __name__ == '__main__':
    resp_data = requests.get(sys.argv[1])
    print(resp_data.headers.get('X-Request-Id'))
