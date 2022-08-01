#!/usr/bin/python3

"""Check if an object is a subclass of a given class"""


def inherits_from(obj, a_class):
    """check if an object is a subclass of a given class

    Args:
       obj (any): The object to be checked
       a_class (type): The class to be check for obj subclass

    Returns:
       True if the obj is a subclass of a_class False otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
