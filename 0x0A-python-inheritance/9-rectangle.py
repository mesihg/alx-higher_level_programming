#!/usr/bin/python3

"""A rectangle that extends geometry class module."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle that extends from geometry."""

    def __init__(self, width, height):
        """initialize rectangle data."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the calculated the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """return the print and str represenation of the Rectangle."""
        rect = "[" + str(self.__class__.__name__) + "] "
        rect += str(self.__width) + "/" + str(self.__height)
        return rect
