#!/usr/bin/env python3
"""Module that adds two matrices"""


def add_matrices(mat1, mat2):
    """Returns the addition of matrices"""
    if not isinstance(mat1, list):
        return mat1 + mat2
    if len(mat1) != len(mat2):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        new_matrix.append(add_matrices(mat1[i], mat2[i]))
    return new_matrix
