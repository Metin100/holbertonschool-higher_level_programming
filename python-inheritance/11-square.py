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

    def area(self):
        """Area function of completing area of giving sizes"""

        return self.__size ** 2

    def __str__(self):
        """print and returning of str function"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
