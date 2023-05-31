#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """x elements of a list

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    printed = 0
    i = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except:
            continue
    print("")
    return printed
