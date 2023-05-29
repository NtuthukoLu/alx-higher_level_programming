#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists of any type (integer, string, etc.)
    Args:
        my_list_1 (list): List of any type
        my_list_2 (list): List of any type
        list_length (int): Can be bigger than the length of both lists
    Returns:
        new_list (list): List of length = list_length with all divisions
    Raises:
        TypeError: If an element is not an integer or float
        ZeroDivisionError: If the division can't be done (/0)
        IndexError: If my_list_1 or my_list_2 is too short
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
            result = 0
        except ZeroDivisionError:
            print('division by 0')
            result = 0
        except IndexError:
            print('out of range')
            result = 0
        finally:
            new_list.append(result)
    return new_list
