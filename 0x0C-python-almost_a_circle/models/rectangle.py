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
