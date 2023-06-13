#!/usr/bin/python3
""" 2-append_write Module """


def append_write(filename="", text=""):
    """appends onto a utf-8 encoded text file"""
    with open(filename, 'a', encoding='utf-8') as myfile:
        return myfile.write(text)
