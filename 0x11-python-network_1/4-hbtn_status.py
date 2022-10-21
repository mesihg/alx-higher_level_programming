#!/usr/bin/python3
""" Fetch data using request """
import request

if __name__ == '__main__':
    resp_data = request('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(resp_data)))
    print("\t- content: {}".format(resp_data.text))
