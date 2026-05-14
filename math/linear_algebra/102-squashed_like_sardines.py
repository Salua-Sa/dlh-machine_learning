#!/usr/bin/env python3
"""Module that concatenates two matrices along a specific axis"""


def cat_matrices(mat1, mat2, axis=0):
    """Returns the concatenate of two matrices along a specific axis"""
    new_matrix = []
    if axis == 0:
        for row in mat1:
            new_matrix.append(row)
        for row in mat2:
            new_matrix.append(row)
        return new_matrix
    if len(mat1) != len(mat2):
        return None
    else:
        for i in range(len(mat1)):
            result = cat_matrices(mat1[i], mat2[i], axis - 1)
        if result is None:
            return None
        new_matrix.append(result)
        return new_matrix
