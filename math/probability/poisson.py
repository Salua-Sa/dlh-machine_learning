#!/usr/bin/env python3
"""This module creates a class Poisson"""


class Poisson:
    """This class represents a poisson distribution"""
    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
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
