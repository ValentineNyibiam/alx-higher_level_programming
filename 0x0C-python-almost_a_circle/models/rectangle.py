#!/usr/bin/python3
from models.base import Base
"""
This is a module that defines a rectangle class
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.height * self.width

    def display(self):
        """
        Prints in stdout the Rectangle instance
        with the character #, considering the x and y offset
        """
        # print the y offset
        for _ in range(self.y):
                print(" ")

        # print each row with the x offset
        for _ in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """
        Returns  [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute of the class
        """
        if (args):
            unpacked_args = {}
            idx = 0

            while idx < len(args):
                if idx == 0:
                    unpacked_args.update({"id": args[0]})
                elif idx == 1:
                    unpacked_args.update({"width": args[1]})
                elif idx == 2:
                    unpacked_args.update({"height": args[2]})
                elif idx == 3:
                    unpacked_args.update({"x": args[3]})
                elif idx == 4:
                    unpacked_args.update({"y": args[4]})
                idx += 1
        elif (kwargs):
            unpacked_args = kwargs

        for key, value in unpacked_args.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of
        the class
        """
        dict_rep = {}
        for key, value in self.__dict__.items():
            dict_rep.update({key.lstrip("__Rectangle__"): value})

        return dict_rep