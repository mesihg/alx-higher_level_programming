#!/usr/bin/python3

"""A test cases for base module."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Unittests for the Base class."""

    def test_base_automatic_id(self):
        self.assertEqual(Base().id, 1)

    def test_base_previous_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_base_with_new_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_base_to_json_string_none(self):
        base_to_json = Base.to_json_string(None)
        self.assertEqual(base_to_json, "[]")

    def test_base_to_json_string_empty_list(self):
        base_to_json = Base.to_json_string([])
        self.assertEqual(base_to_json, '[]')

    def test_base_to_json_string_list(self):
        base_to_json = Base.to_json_string([{'id': 10}])
        self.assertIsInstance(base_to_json, str)

    def test_base_to_json_string_return_string(self):
        base_to_json = Base.to_json_string([{'id': 10}])
        self.assertEqual(base_to_json, '[{"id": 10}]')

    def test_base_from_json_string_none(self):
        base_from_json = Base.from_json_string(None)
        self.assertEqual(base_from_json, [])

    def test_base_from_json_string_empty_list(self):
        base_from_json = Base.from_json_string('[]')
        self.assertEqual(base_from_json, [])

    def test_base_from_json_string_empty_list(self):
        base_from_json = Base.from_json_string('[{"id": 10}]')
        self.assertEqual(base_from_json, [{"id": 10}])


if __name__ == "__main__":
    unittest.main()
