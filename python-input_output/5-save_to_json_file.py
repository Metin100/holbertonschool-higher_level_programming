#!/usr/bin/python3
"""File"""
import json


def save_to_json_file(my_obj, filename):
    """Function of Object to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        a = json.dumps(my_obj)
        return f.write(a)
