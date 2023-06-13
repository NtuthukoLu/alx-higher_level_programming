#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
