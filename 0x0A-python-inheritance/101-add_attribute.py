#!/usr/bin/python3
"""set a new attribute to an object"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if its possible"""
    if not hasattr(name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
