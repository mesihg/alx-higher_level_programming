#!/usr/bin/python3

"""A square that extends Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that extends from rectangle"""

    def __init__(self, size):
        """initialize square data"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the calculated the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """return the print and str represenation of the square"""
        sqr = "[" + str(self.__class__.__name__) + "] "
        sqr += str(self.__size) + "/" + str(self.__size)
        return sqr
