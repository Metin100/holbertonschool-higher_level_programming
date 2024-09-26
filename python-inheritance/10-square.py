#!/usr/bin/python3
"""File of creating Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class of square"""
    def __init__(self, size):
        """function of initing"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
