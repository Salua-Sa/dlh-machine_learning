#!/usr/bin/env python3
"""This module sets the index of a pandas DataFrame"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Return bitstamp rows concatenated above coinbase rows"""
    df2 = index(df2)
    df1 = index(df1)
    df2 = df2.loc[:1417411920]
    frames = [df2, df1]
    df = pd.concat(frames, keys=["bitstamp", "coinbase"])
    return df
