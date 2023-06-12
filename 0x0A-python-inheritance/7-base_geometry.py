#!/usr/bin/python3
"""7 base geometry module"""


class BaseGeometry():
    """Base Geometry class"""
    def area(self):
        """ raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
