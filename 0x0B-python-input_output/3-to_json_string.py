#!/usr/bin/python3
"""
This module contains a function that returns
the JSON representation of an object (string)
"""
import join


def to_json_string(my_obj):
    """Convert JSON to string"""
    return json.dumps(my_obj)
