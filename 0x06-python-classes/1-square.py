#!/usr/bin/python3
"""This is the square class!"""


class Square:
    """Class defines a square"""

    def __init__(self, size=0):
        """This initializes a square with a size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
