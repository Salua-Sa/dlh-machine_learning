#!/usr/bin/env python3
"""Module that concatenates two matrices along a specific axis"""


def cat_matrices(mat1, mat2, axis=0):
    """Returns the concatenate of two matrices along a specific axis"""
    if len(mat1) != len(mat2):
        return None
    if axis == 0:
        return mat1 + mat2
    else:
        new_matrix = []
        for i in range(len(mat1)):
            new_matrix.append(cat_matrices(mat1[i], mat2[i], axis - 1))
