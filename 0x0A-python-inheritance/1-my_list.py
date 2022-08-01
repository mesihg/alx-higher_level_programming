#!/usr/bin/python3

"""A Myclass Module"""


class MyList(list):
    """A class which inherits from a list"""

    def __init__(self):
        """initialize data here"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
