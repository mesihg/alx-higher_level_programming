#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_empty_list_value(self):
        """Test max value with empty list"""
        self.assertIsNone(max_integer([]))

    def test_empty_argument(self):
        """Test max value with empty argument"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test max value with one value in the list"""
        self.assertEqual(max_integer([4]), 4)

    def test_max_end(self):
        """Test max value when the max value is at the end of the list"""
        self.assertEqual(max_integer([6, 63, 12, 90, 34, 150]), 150)

    def test_max_middle(self):
        """Test max value when the max value is at the middle of the list"""
        self.assertEqual(max_integer([2, 10, 8, 360, 14, 50]), 360)

    def test_max_start(self):
        """Test max value when the max value is at the start of the list"""
        self.assertEqual(max_integer([100, 50, 78, 89, 12, 39]), 100)

    def test_max_with_negative(self):
        """Test max value with one negative value of the list"""
        self.assertEqual(max_integer([2, 10, 8, -360, 14, 50]), 50)

    def test_max_with_all_negative(self):
        """Test max value with all negative value of the list"""
        self.assertEqual(max_integer([-9, -20, -35, -76, -10]), -9)

    def test_max_with_none(self):
        """Test max value with none argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_max_with_non_integer(self):
        """Test max value with non-integer value of the list"""
        with self.assertRaises(TypeError):
            max_integer(["test", 1, 2, 3, 4, 5])
