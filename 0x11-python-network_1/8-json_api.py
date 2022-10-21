#!/usr/bin/python3
""" "Make a post request with searching data"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv[1]) == 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    resp_data = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        response = resp_data.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
