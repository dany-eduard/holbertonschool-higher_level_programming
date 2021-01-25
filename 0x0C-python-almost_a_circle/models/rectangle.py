#!/usr/bin/python3
"""This module contains the Rectangle Class"""
from models.base import Base


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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self, value):
        """Getter - obtain the height of the rectangle"""
        return self.height

    @height.setter
    def height(self, value):
        """Setter - define the height value of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self, value):
        """Getter - obtain the x value of the rectangle"""
        return self.x

    @height.setter
    def x(self, value):
        """Setter - define the x value of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, value):
        """Getter - obtain the y value of the rectangle"""
        return self.x

    @height.setter
    def y(self, value):
        """Setter - define the y value of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
