#!/usr/bin/python3
"""
This is a module that defines a Student class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if (type(attrs) == list):
            return_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    return_dict[key] = value
            return dict(sorted(return_dict.items()))
        return dict(sorted(self.__dict__.items()))

    def reload_from_json(self, json):
        """
         Replaces all attributes of the Student instance
        """
        for key_json, val_json in json.items():
            for key_obj, val_obj in self.__dict__.items():
                if key_json == key_obj:
                    self.__dict__[key_obj] = val_json

