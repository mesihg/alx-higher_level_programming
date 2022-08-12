#!/usr/bin/python3

"""A test cases for square module."""


import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for the Square class."""

    def test_square_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_square_two_args(self):
        sqr = Square(1, 2)
        self.assertIsInstance(sqr, Base)

    def test_square_three_args(self):
        sqr = Square(1, 2, 3)
        self.assertIsInstance(sqr, Base)

    def test_square_string_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_square_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_square_four_args(self):
        sqr = Square(1, 2, 3, 4)
        self.assertIsInstance(sqr, Base)

    def test_square_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_square_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_square_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_str_all_valid(self):
        sqr = Square(10, 20, 3, 4)
        test = "[Square] ({}) {}/{} - {}".format(
            sqr.id, sqr.x, sqr.y, sqr.width)
        self.assertEqual(test, sqr.__str__())

    def test_square_str_size_new_attributes(self):
        sqr = Square(10, 20, 5, 6)
        sqr.size = 5
        test = "[Square] (6) 20/5 - 5"
        self.assertEqual(test, sqr.__str__())

    def test_square_to_dictionary(self):
        sqr = Square(2, 3, 5, 6)
        dict_test = {'x': 3, 'y': 5, 'id': 6, 'size': 2}
        self.assertDictEqual(dict_test, sqr.to_dictionary())

    def test_square_update_0(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sqr))

    def test_square_update_1(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(sqr))

    def test_square_update_2(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 1)
        self.assertEqual("[Square] (89) 10/10 - 1", str(sqr))

    def test_square_update_3(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 1, 2)
        self.assertEqual("[Square] (89) 2/10 - 1", str(sqr))

    def test_square_update_4(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 1, 2, 3)
        self.assertEqual("[Square] (89) 2/3 - 1", str(sqr))

    def test_square_update_5(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(**{'id': 90})
        self.assertEqual("[Square] (90) 10/10 - 10", str(sqr))

    def test_square_update_6(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(**{'id': 87, 'size': 1})
        self.assertEqual("[Square] (87) 10/10 - 1", str(sqr))

    def test_square_update_7(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(**{'id': 80, 'size': 1, 'x': 2})
        self.assertEqual("[Square] (80) 2/10 - 1", str(sqr))

    def test_square_update_8(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(**{'id': 81, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual("[Square] (81) 2/3 - 1", str(sqr))

    def test_square_create0(self):
        sqr = Square.create(**{'id': 82})
        self.assertEqual("[Square] (82) 0/0 - 1", str(sqr))

    def test_square_create1(self):
        sqr = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual("[Square] (89) 0/0 - 1", str(sqr))

    def test_square_create2(self):
        sqr = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual("[Square] (89) 2/0 - 1", str(sqr))

    def test_square_create3(self):
        sqr = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual("[Square] (89) 2/3 - 1", str(sqr))

    def test_square_save_to_file_none(self):
        Square.save_to_file(None)
        output = Square.load_from_file()
        self.assertEqual(output, [])

    def test_square_save_to_file_empty_list(self):
        Square.save_to_file([])
        output = Square.load_from_file()
        self.assertEqual(output, [])

    def test_square_save_to_file_list(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertTrue(os.path.exists("Square.json"), True)

    def test_square_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

    def test_square_load_from_file(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertTrue(os.path.exists("Square.json"), True)


if __name__ == "__main__":
    unittest.main()
