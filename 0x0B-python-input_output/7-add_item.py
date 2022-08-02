#!/usr/bin/python3
"""Add all arguments to a Python list, and then save them to a file"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


for item in range(1, len(argv) + 1):
    save_to_json_file(item, 'add_item.json')
load_from_json_file('add_item.json')
