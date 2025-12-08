from models.rectangle import Rectangle
"""
This is a module that defines a Rectangle class
"""

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.__width = value
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns [Square] (<id>) <x>/<y> - <size>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.size}"

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
                    unpacked_args.update({"size": args[1]})
                elif idx == 2:
                    unpacked_args.update({"x": args[2]})
                elif idx == 3:
                    unpacked_args.update({"y": args[3]})
                idx += 1
        elif (kwargs):
            unpacked_args = kwargs

        for key, value in unpacked_args.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
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
            dict_rep.update({key.lstrip("Rectangle__"): value})

        if "height" in dict_rep:
            del dict_rep["height"]
        if "width" in dict_rep:
            size_value = dict_rep.pop("width")
            dict_rep.update({"size": size_value})

        return dict_rep