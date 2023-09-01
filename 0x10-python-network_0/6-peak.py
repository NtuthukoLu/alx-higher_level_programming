#!/usr/bin/python3
"""Finds peak of ints 
"""
def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
