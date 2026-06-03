#!/usr/bin/env python3
"""Module calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """Returns the derivative of a polynomia"""
    if not isinstance(poly, list):
        return None
    new_list = []
    for i in range(len(poly)):
        if i >= 1:
            new_list.append(poly[i] * i)
    return new_list
