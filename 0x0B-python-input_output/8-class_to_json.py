#!/usr/bin/python3

"""A function that returns a dictionary description of a class"""


def class_to_json(obj):
    """returns a dictionary description of obj

    Args:
       obj: an instance of a class

    Returns:
        dictionary description of obj
    """

    return obj.__dict__
