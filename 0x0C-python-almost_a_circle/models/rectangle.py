#!/usr/bin/python3
"""This module contains the Rectangle Class"""
from models.base import Base


def validate_int(prop, value):
    """Check value"""
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(prop))
    elif prop == "width" or prop == "height" and value <= 0:
        raise ValueError("{} must be > 0".format(prop))
    elif prop == "x" or prop == "y" and value < 0:
        raise ValueError("{} must be >= 0".format(prop))


class Rectangle(Base):
    """Rectangle Class extends from Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attributes"""
        self.width = width
        self.heigth = height
        self.x = x
        self.y = x
        super().__init__(id)

    @property
    def width(self):
        """Getter - obtain the width of the rectangle"""
        return self.width

    @width.setter
    def width(self, value):
        """Setter - define the width value of the rectangle"""
        validate_int("width", value)
        self._width = value

    @property
    def height(self, value):
        """Getter - obtain the height of the rectangle"""
        return self.height

    @height.setter
    def height(self, value):
        """Setter - define the height value of the rectangle"""
        validate_int("height", value)
        self.__height = value

    @property
    def x(self, value):
        """Getter - obtain the x value of the rectangle"""
        return self.x

    @height.setter
    def x(self, value):
        """Setter - define the x value of the rectangle"""
        validate_int("x", value)
        self.__x = value

    @property
    def y(self, value):
        """Getter - obtain the y value of the rectangle"""
        return self.x

    @height.setter
    def y(self, value):
        """Setter - define the y value of the rectangle"""
        validate_int("y", value)
        self.__y = value
