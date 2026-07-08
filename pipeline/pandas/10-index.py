#!/usr/bin/env python3
"""This module sets the index of a pandas DataFrame"""


def index(df):
    """Returns a DataFrame with Timestamo set as the index"""
    df = df.set_index('Timestamp')
    return df
