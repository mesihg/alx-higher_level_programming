#!/usr/bin/python3

"""A Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """A rectangle class that extends Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns width of a rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of a rectangle instance"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height of a rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of a rectangle instance"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x attribute of a rectangle instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x attribute of a rectangle instance"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y attribute of a rectangle instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y attribute of a rectangle instance"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle instance with character #"""
        if self.width == 0 or self.height:
            print()
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """returns string representation of the object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update each attributes of Rectangle class"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs is not None:
            for k, val in kwargs.items():
                setattr(self, k, val)

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
