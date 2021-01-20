#!/usr/bin/python3
"""This module contains the Square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square subclass
    """

    def __init__(self, size):
        """Instatiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return Rectangle's area
        """
        return self.__size * self.__size
