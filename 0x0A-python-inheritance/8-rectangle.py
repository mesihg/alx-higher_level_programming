#!/usr/bin/python3

"""A rectangle that extends geometry class module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle that extends from geometry"""
    def __init__(self, width, height):
        """initialize rectangle data"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
