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

    def __eq__(self, other):
        """compares whether two square instances are equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """compares whether two squares are not equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """compares whether one square is greater than the other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """compares whether one square is greater or equal to the other"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """compares whether one square is less than the other"""
        return self.area() < other.area()

    def __le__(self, other):
        """compares whether one square is less or equal to the other"""
        return self.area() <= other.area()
