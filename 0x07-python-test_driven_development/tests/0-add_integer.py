#!/usr/bin/python3
""" 0-add_integer module """


def add_integer(a, b=98):
    """ Addition Function """
    if type(a) != [int, float]:
        raise TypeError("a must be an integer")
    if type(b) != [int, float]:
        raise TypeError("b must be an integer")
    return a + b
