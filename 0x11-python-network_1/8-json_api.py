#!/usr/bin/python3
""" "Make a post request with searching data"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        param = ""
    else:
        param = sys.argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data={'q': param})
    try:
        response = resp.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
