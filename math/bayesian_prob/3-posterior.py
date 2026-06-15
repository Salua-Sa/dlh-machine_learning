#!/usr/bin/env python3
"""Module that calculates the posterior probability"""
import numpy as np


def posterior(x, n, P, Pr):
    """Reaturn the posterior probability for the various hypothetical"""
    """probabilities of developing severe side effects given the data"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is " +
                         "greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    for i in P:
        if i < 0 or i > 1:
            raise ValueError("All values in P must be in the range [0, 1]")
    for i in Pr:
        if i < 0 or i > 1:
            raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    factorial_x = 1
    factorial_n = 1
    factorial_n_minos_s = 1
    n_minus_x = n - x
    x_original = x
    n_original = n
    while x > 0:
        factorial_x *= x
        x -= 1
    while n > 0:
        factorial_n *= n
        n -= 1
    while n_minus_x > 0:
        factorial_n_minos_s *= n_minus_x
        n_minus_x -= 1
    comb = factorial_n / (factorial_x * factorial_n_minos_s)
    likelihood = (comb
                  * (P ** x_original)
                  * ((1 - P) ** (n_original - x_original)))
    intersection = likelihood * Pr
    marginal = np.sum(intersection)
    return (intersection / marginal)
