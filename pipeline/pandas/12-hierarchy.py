#!/usr/bin/env python3
"""This module concatenates two pandas DataFrame using a hierarchical index"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Return concatenated DataFrames with Timestamp as first index level"""
    df2 = index(df2)
    df1 = index(df1)
    df2 = df2.loc[1417411980: 1417417980]
    df1 = df1.loc[1417411980: 1417417980]
    frames = [df2, df1]
    df = pd.concat(frames, keys=["bitstamp", "coinbase"])
    df = df.swaplevel()
    df = df.sort_index()
    return df
