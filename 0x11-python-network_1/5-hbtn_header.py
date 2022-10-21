#!/usr/bin/python3
""" Fetch data using request and displays the value of X-Request-Id """
import requests

if __name__ == '__main__':
    resp_data = requests.get('https://alx-intranet.hbtn.io/status')
    print(resp_data.headers['X-Request-Id'])
