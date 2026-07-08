#!/usr/bin/env python3
"""This module removes entries whre a specific column has NaN values"""


def prune(df):
    """Returns a DataFrame after removing any entries"""
    df = df.dropna(how="any")
    return df
