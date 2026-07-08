#!/usr/bin/env python3
"""This module sorts a DataFrame"""


def high(df):
    """Returns a sorted DataFrame by the High price in descending order"""
    df = df.sort_values(by="High", ascending=False)
    return df
