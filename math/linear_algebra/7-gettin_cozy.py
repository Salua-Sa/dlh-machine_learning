#!/usr/bin/env python3
"""Module that concatenates two matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Returns the concaten´stes of two matrices"""
    new_matrix = []
    if axis == 0:
        for row in mat1:
            new_matrix.append(row[:])
        for row in mat2:
            new_matrix.append(row[:])
    if axis == 1:
        for i in range(len(mat1)):
            new_row = []
            new_row.append(mat1[i] + mat2[i])
            new_matrix.append(new_row)
    return new_matrix
