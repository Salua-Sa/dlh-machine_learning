#!/usr/bin/env python3
"""This module calculates a correlation matrix"""
import numpy as np


def correlation(C):
    """Return a correlation matrix of a covariance matrix C."""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    variances = np.diag(C)
    stddev = np.sqrt(variances)
    denominator = np.outer(stddev, stddev)
    corr = C / denominator

    return corr
