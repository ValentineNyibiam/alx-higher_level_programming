#!/usr/bin/python3
"""
This is a module that defines a Student class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return dict(sorted(self.__dict__.items()))
