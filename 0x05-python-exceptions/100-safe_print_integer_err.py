#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints an integer value followed by a new line.
    Returns True if value is an integer and False otherwise.
    If False, prints an error message preceded by "Exception:" to stderr.

    Parameters:
    value (any type): Value to be printed

    Returns:
    bool: True if value is an integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        print("Exception: {}".format(sys.exc_info()[0]), file=sys.stderr)
        return False
