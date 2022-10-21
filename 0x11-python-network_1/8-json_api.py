#!/usr/bin/python3
""" "Make a post request with searching data"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv[1]) == 1:
        search_param = {'q': sys.argv[1]}
    else:
        search_param = {'q': ""}
    resp_data = requests.post("http://0.0.0.0:5000/search_user", data=search_param)
    try:
        response = resp_data.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
