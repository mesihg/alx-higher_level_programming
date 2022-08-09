#!/usr/bin/python3

"""A test cases for rectangle module."""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for the Rectangle class."""

    def test_rectangle(self):
        rect = Rectangle(1, 2)
        self.assertEqual()
   

if __name__ == "__main__":
    unittest.main()
