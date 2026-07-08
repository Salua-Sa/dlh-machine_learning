#!/usr/bin/env python3
"""This module sorts a DataFrame"""


def high(df):
    """Returns a sorted DataFrame by the High price in descending order"""
    df = df.sort_values(by="High", ascending=False)
    return df

from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df = high(df)
print(df.head())