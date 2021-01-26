#!/usr/bin/python3
"""This module contains the Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class extends from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter - obtain the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Getter - obtain the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Getter - obtain the x value of the rectangle"""
        return self.__x

    @property
    def y(self):
        """Getter - obtain the y value of the rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter - define the width value of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter - define the height value of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter - define the x value of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter - define the y value of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print Rectagle using #"""
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        """Returns the str representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes"""
        if len(args) > 0:
            attr = ["id", "width", "height", "x", "y"]
            for key, value in enumerate(args):
                setattr(self, attr[key], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
