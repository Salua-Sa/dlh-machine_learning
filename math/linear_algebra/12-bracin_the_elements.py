#!/usr/bin/env python3
"""Module that perfoms element-wise operations"""


def np_elementwise(mat1, mat2):
    """Returns +, -, *, / element-wise"""
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
