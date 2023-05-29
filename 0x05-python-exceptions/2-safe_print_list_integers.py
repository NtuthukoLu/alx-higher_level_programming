#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Parameters:
    my_list (list): Contains any type (integer, string, etc.)
    x (int): Number of elements to access in my_list

    Returns:
    int: The real number of integers printed

    Raises:
    Exception: If x is greater than the length of my_list
    """
    elements_printed = 0
    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]),end ='')
            elements_printed += 1
        except (ValueError, TypeError):
            pass
    return elements_printed
