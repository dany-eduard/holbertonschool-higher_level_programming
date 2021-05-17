#!/usr/bin/python3
"""This module contains the Base Class"""
import json
import csv
from os import path


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

    @staticmethod
    def from_json_string(json_string):
        """Return the JSON string to a list of dictionary"""
        if json_string is None and not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a "dummy" instance and updates the
        value of the attributes with those of the given dictionary
        and returns a new object with all attributes already set
        """
        filename = cls.__name__ + ".csv"
        csvlist = []
        if list_objs:
            for i in list_objs:
                dic = i.to_dictionary()
                if cls.__name__ == "Rectangle":
                    csvlist.append([dic["id"], dic["width"],
                                    dic["height"], dic["x"], dic["y"]])

                elif cls.__name__ == "Square":
                    csvlist.append([dic["id"], dic["size"],
                                    dic["x"], dic["y"]])

        with open(filename, "w", encoding="utf-8") as myfile:
            w = csv.writer(myfile)
            w.writerows(csvlist)

    @classmethod
    def load_from_file(cls):
        """Determine if the file exist and return a list of instances (objs)"""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, encoding="utf-8") as myfile:
                r = csv.reader(myfile)
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    attr = ["id", "size", "x", "y"]
                inslist = []
                for row in r:
                    ct, dic = 0, {}
                    for i in row:
                        dic[attr[ct]] = int(i)
                        ct += 1
                    inslist.append(cls.create(**dic))
                return inslist
        except IOError:
            return []
