#!/usr/bin/env python3
"""Module that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """Returns the integral of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0 or not isinstance(C, int):
        return None
    new_list = []
    new_list.append(C)
    for i in range(len(poly)):
        if poly[i] == 0:
            new_list.append(0)
        else:
            result = (poly[i] / (i + 1))
            if result.is_integer():
                new_list.append(int(result))
            else:
                new_list.append(result)
    while len(new_list) > 1 and new_list[-1] == 0:
        new_list.pop()
    return new_list
