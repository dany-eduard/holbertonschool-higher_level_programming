#!/usr/bin/python3
"""This module contains the BaseGeometry Class"""


class BaseGeometry:
    """
    BaseGeometry Class
    """

    def are(self):
        """
        Public instance method that raises an Exception with the message
        """
        raise Exeption('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method that validates value

        Args:
            name (str): you can assume name is always a string
            value (int): validate, must be an int

        Raises:
            TypeError: if value is not an integer: raise a TypeError \
                exception, with the message <name> must be an integer.
            ValueError: if value is less or equal to 0: raise a ValueError \
                exception with the message <name> must be greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
