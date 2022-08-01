#!/usr/bin/python3

"""Check if an object is an instance of a given class"""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance of a given class

    Args:
       obj (any): The object to be checked
       a_class (type): The class to be check for obj instance

    Returns:
       True if the obj is an instance of a_class False otherwise
    """
    return isinstance(obj, a_class)
