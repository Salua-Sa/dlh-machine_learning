#!/usr/bin/env python3
"""This module creates a pandas DataFrame from a Numpy array"""
import pandas as pd


def from_numpy(array):
    """Return a DataFrame created from a NunmPy array"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_of_columns = array.shape[1]
    if number_of_columns > 26:
        columns = list(letters[:number_of_columns])
    else:
        columns = list(letters[:number_of_columns])
    df = pd.DataFrame(array, columns=columns)
    return df
