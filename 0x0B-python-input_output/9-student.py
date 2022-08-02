#!/usr/bin/python3

"""Student class module"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """initialize student class with data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary description of student class"""
        return self.__dict__
