#!/usr/bin/python3

"""A test cases for rectangle module."""

import io
import os
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for the Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_rectangle_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_two_args(self):
        rect = Rectangle(1, 2)
        self.assertIsInstance(rect, Base)

    def test_rectangle_three_args(self):
        rect = Rectangle(1, 2, 3)
        self.assertIsInstance(rect, Base)

    def test_rectangle_four_args(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(rect, Base)

    def test_rectangle_five_args(self):
        rect = Rectangle(1, 2, 3, 4, 6)
        self.assertIsInstance(rect, Base)

    def test_rectangle_string_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 4)

    def test_rectangle_string_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "4")

    def test_rectangle_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, "4")

    def test_rectangle_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 5, "4")

    def test_rectangle_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 3, -4)

    def test_rectangle_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 3, 5, -4)

    def test_rectangle_area_valid(self):
        rect = Rectangle(10, 20, 3, 4, 5)
        self.assertEqual(200, rect.area())

    def test_rectangle_area_args(self):
        rect = Rectangle(10, 20, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.area('10')

    def test_rectangle_str_all_valid(self):
        rect = Rectangle(10, 20, 3, 4, 5)
        test = "[Rectangle] ({}) {}/{} - {}/{}".format(
            rect.id, rect.x, rect.y, rect.width, rect.height)
        self.assertEqual(test, rect.__str__())

    def test_rectangle_str_width_height_new_attributes(self):
        rect = Rectangle(10, 20, 5, 6, 9)
        rect.width = 5
        rect.height = 19
        test = "[Rectangle] (9) 5/6 - 5/19"
        self.assertEqual(test, rect.__str__())

    def test_rectangle_str_args(self):
        rect = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rect.__str__(5, 5)

    def test_rectangle_display_x(self):
        rect = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle.capture_stdout(rect, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_rectangle_display_y(self):
        rect = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle.capture_stdout(rect, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_rectangle_display_no_x_y(self):
        rect = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle.capture_stdout(rect, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_rectangle_display_x_y(self):
        rect = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle.capture_stdout(rect, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_rectangle_display_args(self):
        rect = Rectangle(2, 4, 3, 2, 0)
        with self.assertRaises(TypeError):
            rect.display(1, 2)

    def test_rectangle_to_dictionary(self):
        rect = Rectangle(2, 3, 5, 6, 7)
        dict_test = {'x': 5, 'y': 6, 'id': 7, 'height': 3, 'width': 2}
        self.assertDictEqual(dict_test, rect.to_dictionary())

    def test_rectangle_update_0(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect))

    def test_rectangle_update_1(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_rectangle_update_2(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(6, 98)
        self.assertEqual("[Rectangle] (6) 10/10 - 98/10", str(rect))

    def test_rectangle_update_3(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(6, 98, 1)
        self.assertEqual("[Rectangle] (6) 10/10 - 98/1", str(rect))

    def test_rectangle_update_4(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(6, 98, 1, 1)
        self.assertEqual("[Rectangle] (6) 1/10 - 98/1", str(rect))

    def test_rectangle_update_5(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(**{'id': 90})
        self.assertEqual("[Rectangle] (90) 10/10 - 10/10", str(rect))

    def test_rectangle_update_6(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(**{'id': 90, 'width': 1})
        self.assertEqual("[Rectangle] (90) 10/10 - 1/10", str(rect))

    def test_rectangle_update_7(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual("[Rectangle] (89) 10/10 - 1/2", str(rect))

    def test_rectangle_update_8(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual("[Rectangle] (89) 10/10 - 1/2", str(rect))

    def test_rectangle_update_9(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual("[Rectangle] (89) 3/10 - 1/2", str(rect))

    def test_rectangle_update_10(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(rect))

    def test_rectangle_update_11(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(rect))

    def test_rectangle_create0(self):
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual("[Rectangle] (89) 0/0 - 1/1", str(rect))

    def test_rectangle_create1(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual("[Rectangle] (89) 0/0 - 1/1", str(rect))

    def test_rectangle_create2(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual("[Rectangle] (89) 0/0 - 1/2", str(rect))

    def test_rectangle_create3(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual("[Rectangle] (89) 0/0 - 1/2", str(rect))

    def test_rectangle_create4(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual("[Rectangle] (89) 3/0 - 1/2", str(rect))

    def test_rectangle_create5(self):
        rect = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(rect))

    def test_rectangle_save_to_file_none(self):
        Rectangle.save_to_file(None)
        output = Rectangle.load_from_file()
        self.assertEqual(output, [])

    def test_rectangle_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        output = Rectangle.load_from_file()
        self.assertEqual(output, [])

    def test_rectangle_save_to_file_list(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(os.path.exists("Rectangle.json"), True)

    def test_rectangle_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

    def test_rectangle_load_from_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(os.path.exists("Rectangle.json"), True)


if __name__ == "__main__":
    unittest.main()
