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
