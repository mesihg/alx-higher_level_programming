#!/usr/bin/python3

"""A Base class module"""

import json
import csv


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance data

        Args:
           id (int): An id assigned to Base instance

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file:"""
        filename = cls.__name__ + ".json"
        object_list = []

        if list_objs is not None:
            for objs in list_objs:
                object_list.append(objs.to_dictionary())
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(object_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list represented by json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                object_list = cls.from_json_string(f.read)
                for dcts in object_list:
                    instance_list.append(cls.create(**dcts))
                return instance_list
        except Exception:
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialization of a list of objects to a csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialization of a list of objects from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
