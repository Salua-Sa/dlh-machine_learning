#!/usr/bin/env python3
"""This module modifies a pandas DataFrame"""
import pandas as pd


def rename(df):
    """Return a modified pandas DataFrame with Datatime and Close columns"""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df['Datetime'] = pd.to_datetime(df["Datetime"], unit="s")
    df = df[["Datetime", "Close"]]
    return df
