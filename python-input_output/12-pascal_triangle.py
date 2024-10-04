#!/usr/bin/python3
"""File"""


def pascal_triangle(n):
    """Function of reckoning pascal triangle"""
    list = []
    if n > 0:
        for i in range(n):
            pascal = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    pascal.append(1)

                else:
                    pascal.append(list[i - 1][j - 1] + list[i - 1][j])
            list.append(pascal)
    return list
