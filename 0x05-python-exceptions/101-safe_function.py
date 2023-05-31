#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely and returns the result of the function.
    If something happens during the function, returns None and prints in stderr the error preceded by Exception.
    """
    try:
        return fct(*args)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
