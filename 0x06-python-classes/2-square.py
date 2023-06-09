#!/usr/bin/python3
"""Define a Class"""


class Square:
    """ Clases defines a square"""

    def __init__(self, size=0):
        """the initialization of a square and size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Prints area"""
        return self.__size ** 2
