#!/usr/bin/python3
"""This module contains the MyList class"""


class MyList(list):
    """This class inherits from list

    Args:
        list (class)
    """
    def print_sorted(self):
        """This method print the sorted list"""
        print(sorted(self))
