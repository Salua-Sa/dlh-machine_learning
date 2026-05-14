#!/usr/bin/env python3
"""Module that concatenates two matrices along a specific axis"""


def cat_matrices(mat1, mat2, axis=0):
    """Returns the concatenate of two matrices along a specific axis"""
    shape1 = np.shape(mat1)
    shape2 = np.shape(mat2)
    if len(shape1) != len(shape2) or axis >= len(shape1):
        return None
    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None
    if axis == 0:
        if len(mat1) != len(mat2):
            return None
        return mat1 + mat2
    new_matrix = []
    for i in range(len(mat1)):
         new_matrix.append(cat_matrices(mat1[i] + mat2[i], axis - 1))
