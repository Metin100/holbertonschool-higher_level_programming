#!/usr/bin/python3
"""File"""
import json


def load_from_json_file(filename):
    """function of getting json file string to object"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
