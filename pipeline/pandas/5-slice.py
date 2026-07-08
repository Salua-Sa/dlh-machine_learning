#!/usr/bin/env python3
"""This module extracts a selected DataFrame colums and a specific row"""


def slice(df):
    """Returns a sliced pandas DataFrame"""
    df = df.loc[::60, ["High", "Low", "Close", "Volume_(BTC)"]]
    return df
