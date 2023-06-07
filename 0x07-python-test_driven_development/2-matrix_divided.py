#!/usr/bin/python3
""" 2-matrix_divided Module """


def matrix_divided(matrix, div):
    """ Divides matrix on lists """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
        return matrix
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    prevRowLen = -1
    new_list = []
    for row in matrix:
        if (prevRowLen != len(row) and prevRowlen != -1):
            raise TypeError("Each row of the matric have the same size")
            return matrix
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of" + " integers/floats")
            return matrix
        else:
            mew_list.append(round(element / div,2))
        prevRowLen = len(row)

    return new_list
