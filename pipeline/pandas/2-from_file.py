#!/usr/bin/env python3
"""This module loads data from a file as a pandas DataFrame"""
import pandas as pd


def from_file(filename, delimiter):
    """Return data from a file as a pandas DataFrame"""
    df = pd.read_csv(filename, delimiter=delimiter)
    return df
