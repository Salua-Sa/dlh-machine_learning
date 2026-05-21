#!/usr/bin/env python3
"""Module that calculates the inverse of a matrix"""


def inverse(matrix):
    """Returns the inverse of the matrix"""
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if len(row) != len(matrix) or matrix == [[]]:
            raise ValueError("matrix must be a non-empty square matrix")
    inverse_matrix = []
    adjugate_matrix = adjugate(matrix)
    det = determinant(matrix)
    if det == 0:
        return None
    result = 0
    for i in range(len(adjugate_matrix)):
        inverse_row = []
        for j in range(len(adjugate_matrix[0])):
            result = (1/det) * adjugate_matrix[i][j]
            inverse_row.append(result)
        inverse_matrix.append(inverse_row)
    return inverse_matrix


def adjugate(matrix):
    """Returns the adjugate of a matrix"""
    adjugate_matrix = []
    cofactor_matrix = cofactor(matrix)
    for i in range(len(cofactor_matrix)):
        adjugate_row = []
        for j in range(len(cofactor_matrix)):
            adjugate_row.append(cofactor_matrix[j][i])
        adjugate_matrix.append(adjugate_row)
    return adjugate_matrix


def cofactor(matrix):
    """Returns the cofactor of a matrix"""
    if len(matrix) == 1:
        return [[1]]
    cofactor_matrix = minor(matrix)
    for i in range(len(cofactor_matrix)):
        for j in range(len(cofactor_matrix)):
            cofactor_sign = (-1) ** (i + j)
            cofactor_matrix[i][j] *= cofactor_sign
    return cofactor_matrix


def minor(matrix):
    """Returns the minor of a matrix"""
    if len(matrix) == 1:
        return [[1]]
    minor_matrix = []
    for i in range(len(matrix)):
        minor_row = []
        for col in range(len(matrix)):
            submatrix = []
            for row_i in range(len(matrix)):
                if row_i != i:
                    new_row = []
                    for j in range(len(matrix[row_i])):
                        if j != col:
                            new_row.append(matrix[row_i][j])
                    submatrix.append(new_row)
                det = determinant(submatrix)
            minor_row.append(det)
        minor_matrix.append(minor_row)
    return minor_matrix


def determinant(matrix):
    """Returns the determinant of a matrix"""
    if matrix == [] or matrix == [[]]:
        return 1
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
