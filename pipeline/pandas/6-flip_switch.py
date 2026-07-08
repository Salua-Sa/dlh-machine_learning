#!/usr/bin/env python3
"""This module sorts and transposes a DataFrame"""


def flip_switch(df):
    """Returns a transformed pandas DataFrame"""
    df = df.sort_index(axis=0, ascending=False).T
    return df
