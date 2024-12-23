#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    Return list of lists of ints representing
    Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for index in range(1, n):
        row = [1]

        for j in range(1, index):
            row.append(triangle[index - 1][j - 1] + triangle[index - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
