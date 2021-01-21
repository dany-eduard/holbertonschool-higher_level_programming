#!/usr/bin/python3
"""
Script that add all arguments to a Python list and then save them to a JSON file
"""
import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    l = load_from_json_file('add_item.json')
except:
    l = []

for i in range(1, len(argv)):
    l.append(argv[i])

save_to_json_file(l, 'add_item.json')
