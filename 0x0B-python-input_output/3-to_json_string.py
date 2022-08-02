#!/usr/bin/python3

"""A function that returns JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """Convert my_obj string to JSON

    Args:
       my_obj (str): string object

    Returns:
       JSON representation of my_obj
    """

    return json.dumps(my_obj)
