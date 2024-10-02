#!/usr/bin/python3
"""File"""
def read_file(filename=""):
    """Function of returning inside of file"""
    with open(filename, encoding = 'utf-8') as f:
        print(f.read())