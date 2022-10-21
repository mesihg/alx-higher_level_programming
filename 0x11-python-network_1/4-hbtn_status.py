#!/usr/bin/python3
""" Fetch data using request """
import requests

if __name__ == '__main__':
    resp_data = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(resp_data.text)))
    print("\t- content: {}".format(resp_data.text))
