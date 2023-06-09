#!/usr/bin/python3
"""square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of Rectangle"""
        return '[' + type(self).__name__ + '] (' + str(self.id) \
            + ') ' + str(self.x) + '/' + str(self.y) + ' - ' \
            + str(self.size)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        key = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, key[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation of
        Rectangle instance
        """
        selfDict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return selfDict

    def to_csv(self):
        """ list containing csv rep of rectangle"""
        return [self.id, self.size, self.x, self.y]

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
