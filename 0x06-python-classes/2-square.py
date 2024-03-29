#!/usr/bin/python3
""" This module defines a class that defines a square """


class Square:
    """ This class defines a square """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
