#!/usr/bin/python3
""" Make a request to GitHub credentials """
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    resp = requests.get('https://api.github.com/user', auth=token)
    print(res.json().get('id'))
