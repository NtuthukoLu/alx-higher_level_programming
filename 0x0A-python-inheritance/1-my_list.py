#!/usr/bin/python3
""" 1-my_list Module """


class MyList(list):
    """Class list"""
    def print_sorted(self):
        """prints in ascending order"""
        copy = self[:]
        copy.sort()
        print(copy)
