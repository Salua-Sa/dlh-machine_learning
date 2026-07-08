#!/usr/bin/env python3
"""This module computes descriptive statistics for a pandas DataFrame"""


def analyze(df):
    """Return a descriptive statistics for all columns """
    """except the Timestamp column"""
    df = df.drop(columns='Timestamp')
    df = df.describe()
    return df
