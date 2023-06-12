#!/usr/bin/python3
""" 10 square Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that extends Rectangle """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
