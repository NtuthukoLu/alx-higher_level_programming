#!/usr/bin/python3
""" 4-inherits_from Module """


def inherits_from(obj, a_class):
    """checks if an object inherited from a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
