#!/usr/bin/python3

"""A Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that extends Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance with a new data"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns size of a square instance"""
        return self.width

    @size.setter
    def size(self, value):
        """set size of a square instance"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns string representation of the object"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update each attributes of Square class"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs is not None:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
