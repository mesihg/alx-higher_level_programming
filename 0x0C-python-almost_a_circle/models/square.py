#!/usr/bin/python3

"""A Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that extends Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, x, y)

    @property
    def size(self):
        """returns size of a square instance"""
        return self.size

    @size.setter
    def size(self, value):
        """set size of a square instance"""
        self.height = value
        self.width = value

    def __str__(self):
        """returns string representation of the object"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update each attributes of Square class"""
        sqr_args = ["id", "height", "x", "y"]
        args_len = len(args)
        if len(args) != 0:
            if args_len > len(sqr_args):
                args_len = len(sqr_args)
            for i in range(args_len):
                setattr(self, sqr_args[i], args[i])
        elif kwargs is not None:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.size
        }
