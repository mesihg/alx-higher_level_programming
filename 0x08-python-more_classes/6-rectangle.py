#!/usr/bin/python3
"""A Rectangle module """


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle instance data"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns printable string representation of rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return ''
        rect_charcter = []
        for i in range(self.__height):
            [rect_charcter.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect_charcter.append('\n')
        return "".join(rect_charcter)

    def __repr__(self):
        """Returns string representation of rectangle instance"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """prints a message when rectangle instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
