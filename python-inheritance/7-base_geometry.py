#!/usr/bin/python3
"""Write and empty class"""


class BaseGeometry:
    """Class of defining public method of area"""
    def area(self):
        """function raises exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Function of raising TypeError or ValueError"""
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
