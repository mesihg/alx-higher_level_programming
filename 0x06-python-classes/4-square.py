#!/usr/bin/python3

"""A Square Entity"""


class Square:
    """Empty class to represent a square"""

    def __init__(self, size=0):
        """Initialize instance data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area of a square"""
        return self.__size**2

    def size(self):
        """returns size of a square"""
        return self.__size

    def size(self, value):
        """sets the size of a square to a new value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
