#!/usr/bin/python3
"""File"""


class Student:
    """Student class"""
    def __init__(self, a, b, c):
        self.first_name = a
        self.last_name = b
        self.age = c

    def to_json(self):
        """function of making to json"""
        return self.__dict__
