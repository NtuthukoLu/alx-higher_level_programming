#!/usr/bin/python3
"""3-rectangle"""


class Rectangle():
    """Defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """initialization of object creation"""
        self.height = height
        self.width = width

    def __str__(self):
        """Returns a printable rep of Rectangle"""
        string = ""
        if 0 in (self.__width, self.__height):
            return ""
        for i in range(self.__height - 1):
            string += "#" * self.__width + "\n"
        string += "#" * self.__width
        return string

    @property
    def height(self):
        """getter for height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height property"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

