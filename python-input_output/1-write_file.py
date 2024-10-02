#!/usr/bin/python3
"""File"""


def write_file(filename="", text=""):
    """Function of writing inside of file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
