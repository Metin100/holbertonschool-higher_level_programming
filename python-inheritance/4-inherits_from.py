#!/usr/bin/python3
"""if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Function of defining object which is inherited"""
    return isinstance(obj, a_class) and type(obj) is not a_class
