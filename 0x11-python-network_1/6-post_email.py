#!/usr/bin/python3
""" Make a post request with data """
import requests
import sys

if __name__ == '__main__':
    resp_data = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(resp_data.text)
