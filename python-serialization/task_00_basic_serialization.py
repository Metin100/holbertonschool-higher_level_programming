#!/usr/bin/python3
"""File"""
import json


def serialize_and_save_to_file(data, filename):
    """Function of serialize and save to exactly file"""
    content = json.dumps(data)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def load_and_deserialize(filename):
    """load from exactly file and deserialize content"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return json.loads(content)