#!/usr/bin/python3
"""Define Square Class For Equaling Size"""


class Square:
    """Class of square"""

    def __init__(self, size=0) -> None:
        """__init__ method that equals size"""
        if isinstance(size,str):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Area method for returning square of size"""
        return self.__size ** 2