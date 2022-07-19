#!/usr/bin/python3

"""A Square Entity"""


class Square:
    """Empty class to represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize instance data"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position with the new position value"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
            return

        [print() for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for a in range(self.__position[0])]
            [print("#", end="") for b in range(self.__size)]
            print()
