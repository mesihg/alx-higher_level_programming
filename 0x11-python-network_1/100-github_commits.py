#!/usr/bin/python3
"""List 10 commits from the most recent to oldest
of the repository 'rails' by the user 'rails'
"""
import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)

    resp = requests.get(url)
    commits = resp.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
