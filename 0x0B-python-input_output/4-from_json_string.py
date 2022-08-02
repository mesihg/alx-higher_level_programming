#!/usr/bin/python3

"""A function that converts a JSON to string"""

import json


def from_json_string(my_str):
    """Convert my_str JSON to string

    Args:
       my_str (obj): JSON object

    Returns:
       JSON decoded to a string
    """

    return json.loads(my_str)
