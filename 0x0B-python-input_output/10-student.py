#!/usr/bin/python3
"""10-student Module"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary """
        dictionary = vars(self)
        if attrs is None:
            return dictionary

        studInfo = {}
        for item in attrs:
            if item in dictionary:
                studInfo[item] = dictionary[item]
        return studInfo
