#!/usr/bin/python3
"""12-pascal_triangle Module"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []
    new_list[]

    for i in range(n):
        row = []
        row.append(1)
        for j in range(2, i + 1):
            row.append(0)
        new_list.append(row)

    back = new_list[0]
    for i in range(1, n):
        for j in range(1, i):
            new_list[i][j] = new_list[i - 1][j - 1] + new_list[i -1][j]
            new_list[i].append[1]
    return new_list
