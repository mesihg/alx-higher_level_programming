#!/usr/bin/python3

"""MagicClass Entity"""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initialize MagicClass instance data"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates area of a MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """calculates circumference of a MagicClass"""
        return (2 * math.pi * self.__radius)
