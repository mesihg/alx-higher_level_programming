#!/usr/bin/python3

"""A Square Entity"""


class Square:
    """Empty class to represent a square"""

    def __init__(self, size=0):
        """Initialize instance data"""
        self.size = size

    def area(self):
        """calculates area of a square"""
        return self.__size**2

    @property
    def size(self):
        """returns size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of a square to a new value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the square with the character #"""
        for i in range(self.__size):
            [print("#", end="") for v in range(self.__size)]
            print()
        if self.__size == 0:
            print()
