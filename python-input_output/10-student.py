#!/usr/bin/python3
"""File"""


class Student:
    """Student class"""
    def __init__(self, a, b, c):
        self.first_name = a
        self.last_name = b
        self.age = c

    def to_json(self, attrs=None):
        """function of making to json"""
        if attrs is None:
            return self.__dict__
        else:
            new = dict()
            for i in attrs:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return new
