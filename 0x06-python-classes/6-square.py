#!/usr/bin/python3


class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization of size of our square class
        """
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position

    @property
    def size(self):
        """
        getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    @property
    def position(self):
        """
        getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position attribute
        """
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square using '#' characters
        also takes into account position (x, y) offsets
        """
        i = 0
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        i = 0
        for i in range(0, self.__size):
            j = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        validates the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
