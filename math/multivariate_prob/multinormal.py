#!/usr/bin/env python3
"""This module creates a multivariate normal distribution class."""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Initialize the distribution from dataset.
        data is a numpy.ndarray of shape (d, n):
        - d = number of dimensions in each data point
        - n = number of data points
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        n = data.shape[1]
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = centered @ centered.T / (n - 1)
