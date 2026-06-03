#!/usr/bin/env python3
"""Module that calculates the definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Returns the definiteness of a matrix"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    shape_matrix = matrix.shape
    if len(shape_matrix) != 2:
        return None
    if shape_matrix[0] != shape_matrix[1]:
        return None
    n = shape_matrix[0]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return None
    result = ""
    d1 = determinant(matrix[:1, :1])
    d2 = determinant(matrix[:2, :2])
    d3 = determinant(matrix)
    if d1 >= 0 and d2 >= 0 and d3 >= 0:
        if d1 == 0 or d2 == 0 or d3 == 0:
            result = "Positive semi-definite"
        else:
            result = "Positive definite"
    elif d1 <= 0 and d2 >= 0:
        if d1 == 0 or d2 == 0 or d3 == 0:
            result = "Negative semi-definite"
        else:
            result = "Negative definite"
    else:
        result = "Indefinite"
    return result


def determinant(matrix):
    """Returns the determinant of a matrix"""
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
