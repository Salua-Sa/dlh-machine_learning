#!/usr/bin/env python3
"""Module that creates a class Binomial"""


class Binomial:
    """This class represents a binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        self.data = data
        self.n = int(n)
        self.p = float(p)
        if n <= 0:
            raise ValueError("n must be a positive value")
        if p <= 0 or p >= 1:
            raise ValueError("p must be greater than 0 and less than 1")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                sum_data = 0
                for i in range(len(data)):
                    sum_data = sum_data + data[i]
                mean = sum_data / len(data)
                variance_sum = 0
                for i in range(len(data)):
                    variance_sum += (data[i] - mean) ** 2
                variance = variance_sum / len(data)
                p = 1 - (variance / mean)
                self.n = round(mean / p)
                self.p = float(mean / self.n)

    def pmf(self, k):
        """Returns the value of the PMF for a given number of successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        n_factorial = 1
        for i in range(1, self.n + 1):
            n_factorial *= i
        k_factorial = 1
        for i in range(1, k + 1):
            k_factorial *= i
        n_minus_k_factorial = 1
        for i in range(1, self.n - k + 1):
            n_minus_k_factorial *= i
        possible_orders = n_factorial / (k_factorial * n_minus_k_factorial)
        return possible_orders * (self.p ** k) * ((1 - self.p) ** (self.n - k))
