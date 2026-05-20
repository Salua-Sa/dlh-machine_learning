#!/usr/bin/env python3
"""Module calculates the determinant of a matrix"""


def determinant(matrix):
    """Returns the determinant of a matrix"""
    if matrix == []:
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    result = 0
    for col in range(len(matrix)):
        submatrix = []
        for row in matrix[1:]:
            new_row = []
            for j in range(len(row)):
                if j != col:
                    new_row.append(row[j])
            submatrix.append(new_row)
        sign = (-1) ** col
        result += sign * matrix[0][col] * determinant(submatrix)
    return result
