#!/usr/bin/python3
"""File"""


def append_write(filename="", text=""):
    """Function of appending text to file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
