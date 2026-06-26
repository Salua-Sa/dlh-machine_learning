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
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = centered @ centered.T / (n - 1)

    def pdf(self, x):
        """Returns the value of the PDF at a data point"""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if x.shape[0] != d or x.shape[1] != 1:
            raise ValueError(f"x must have the shape ({d}, 1)")
        diff = x - self.mean
        inverse_cov = np.linalg.inv(self.cov)
        determinant_cov = np.linalg.det(self.cov)
        exponent = -0.5 * diff.T @ inverse_cov @ diff
        denominator = np.sqrt(((2 * np.pi) ** d) * determinant_cov)
        result_pdf = np.exp(exponent) / denominator
        return result_pdf[0][0]
