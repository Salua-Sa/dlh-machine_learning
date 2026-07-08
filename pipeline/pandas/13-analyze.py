#!/usr/bin/env python3
"""This module concatenates two pandas DataFrame using a hierarchical index"""
import pandas as pd


def analyze(df):
    """Returns a new pd.DataFrame containing these statistics"""
    df = df.drop(columns='Timestamp')
    df = df.describe()
    return df
