#!/usr/bin/python3
"""1-number_of_line module"""


def write_file(filename="", text=""):
    """gets the number of lines from filename"""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
