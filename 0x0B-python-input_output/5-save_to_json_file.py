#!/usr/bin/python3

"""A function that writes an Object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file

    Args:
       filename: name of the file
       my_obj: string content
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
