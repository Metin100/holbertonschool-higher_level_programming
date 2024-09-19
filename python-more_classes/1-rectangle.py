#!/usr/bin/python3
"""Define a class of Rectangle"""


class Rectangle:
    
    def __init__(self, width=0, height=0):
         if not isinstance(width , int):
            raise TypeError("width must be an integer")
         elif width < 0:
            raise ValueError("width must be >= 0")
         if not isinstance(height , int):
            raise TypeError("height must be an integer")
         elif height < 0:
            raise ValueError("height must be >= 0")
         self.__height = height
         self.__width = width

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        if not isinstance(value , int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value , int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
