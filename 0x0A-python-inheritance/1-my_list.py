#!/usr/bin/python3
"""This module contains the MyList class"""


class MyList(list):
    """This method print the sorted list"""
    def print_sorted(self):
        print(sorted(self))
