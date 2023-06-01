#!/usr/bin/python3
""" defines a square by: (based on 6-square.py) """


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a Square with size and position.'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Retrieve the size of the Square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the Square.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Retrieve the position of the Square.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Set the position of the Square.'''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Calculate and return the area of the Square.'''
        return self.__size ** 2

    def my_print(self):
        '''Print the Square with the character '#'.'''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
