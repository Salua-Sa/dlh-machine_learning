#!/usr/bin/env python3
"""This module creates a class Poisson"""


class Poisson:
    """This class represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Inisialization method"""
        self.data = data
        self.lambtha = float(lambtha)
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                sum_data = 0
                for i in range(len(data)):
                    sum_data = sum_data + data[i]
            self.lambtha = sum_data/len(data)

    def pmf(self, k):
        """Returns the PMF for a given number of successes"""
        e = 2.7182818285
        k_factorial = 1
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        original_k = k
        while k > 0:
            k_factorial = k_factorial * (k)
            k = k - 1
        pmf = (e**-self.lambtha * self.lambtha**original_k) / k_factorial
        return pmf

    def cdf(self, k):
        """Returns the CDF for a given number of successes"""
        cdf = 0
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
