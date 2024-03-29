#!/usr/bin/python3

"""A function that creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """creates an object from a JSON file

    Args:
       filename: name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
