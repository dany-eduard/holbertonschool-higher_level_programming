#!/usr/bin/python3
"""This module contains the Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class extends from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter - obtain the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter - define the size value of this Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the str representation of Square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Updates the square attributes"""
        if len(args) > 0:
            attr = ["id", "size", "x", "y"]
            for key, value in enumerate(args):
                if key == 1:
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, attr[key], value)
        else:
            for key, value in kwargs.items():
                if i == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)
