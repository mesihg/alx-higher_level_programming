#!/usr/bin/python3

"""A geometry module"""


class BaseGeometry:
    """A class with public instance method: area(self)"""

    def area(self):
        """raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value if its an integer and  value >= 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
