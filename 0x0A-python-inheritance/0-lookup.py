#!/usr/bin/python3
"""A lookup function module"""


def lookup(obj):
    """return list of available attributes and methods of an object"""
    return dir(obj)
