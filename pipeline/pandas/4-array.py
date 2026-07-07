#!/usr/bin/env python3
"""This module converts a selected DataFrame colums into a Numpy array"""


def array(df):
    """Return the last 10 High and Close values as NumPy array"""
    df = df[["High", "Close"]].tail(10)
    arr = df.to_numpy()
    return arr
