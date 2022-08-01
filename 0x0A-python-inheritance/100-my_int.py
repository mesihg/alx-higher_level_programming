#!/usr/bin/python3

"""MyInt extending int"""


class MyInt(int):
    """Inverting == with != and != with =="""

    def __eq__(self, value):
        """redefine == operator with != operator"""
        return self.real != value

    def __ne__(self, value):
        """redefine != operator with == operator"""
        return self.real == value
