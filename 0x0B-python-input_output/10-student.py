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
        if (type(attrs) == list):
            return_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    return_dict[key] = value
            return dict(sorted(return_dict.items()))
        return dict(sorted(self.__dict__.items()))
