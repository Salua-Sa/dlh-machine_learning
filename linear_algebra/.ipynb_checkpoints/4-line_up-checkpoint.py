#!/usr/bin/env python3
"""Module that adds two arrays element-wise:"""

def add_arrays(arr1, arr2):
    """Returns the addition of two arrays"""
    if len(arr1) != len(arr2):
        return None
    new_array = []

    for i in range(len(arr1)):
        new_array.append(arr1[i] + arr2[i])

    return new_array


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))