#!/usr/bin/python3


def read_file(filename=""):
    """Reads a file"""
    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read(), end='')
