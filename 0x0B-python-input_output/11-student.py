#!/usr/bin/python3

"""Student class module"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """initialize student class with data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary description of student
        instance with the given attrs"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for attr in attrs:
            try:
                new_dict[attr] = self.__dict__[attr]
            except KeyError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except IndexError:
                pass
