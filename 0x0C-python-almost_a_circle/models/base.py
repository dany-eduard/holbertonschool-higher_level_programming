#!/usr/bin/python3
"""This module contains the Base Class"""
import json


class Base:
    """
    This class will be the 'base' of all other classes in this project.
    The goal of it is to manage id attribute in all your future class
    and to avoid duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representationof a list of dict"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Return the JSON string representation of list_objs to a file"""
        json_file = cls.__name__+".json"
        aux_list = []
        if list_objs is not None:
            for i in list_objs:
                aux_list.append(i.to_dictionary())
        with open(json_file, 'w') as f:
            f.write(cls.to_json_string(aux_list))
