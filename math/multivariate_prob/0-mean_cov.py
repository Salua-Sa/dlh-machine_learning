#!/usr/bin/env python3
"""This module calculates the mean and covariance of a data set"""
import numpy as np


def mean_cov(X):
    """Returns the mean and covariance matrix of X.
    X has shape (n, d):
    - n = number of data points
    - d = number of dimensions in each dta point
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n = X.shape[0]
    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(X, axis=0, keepdims=True)
    centered = X - mean
    cov = centered.T @ centered / (n - 1)
    return mean, cov
