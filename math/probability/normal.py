#!/usr/bin/env python3
"""This module Create a class Normal"""


class Normal:
    """This class represents a normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        self.data = data
        self.mean = float(mean)
        self.stddev = float(stddev)
        if stddev <= 0:
            raise ValueError("stddev must be a positive value")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                sum_data = 0
                for i in range(len(data)):
                    sum_data = sum_data + data[i]
            self.mean = sum_data / len(data)
            variance_sum = 0
            for i in range(len(data)):
                variance_sum += (data[i] - self.mean) ** 2
            variance = variance_sum / len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """Returns the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Returns the x-value of a given z-score"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Returns the value of the PDF for a given x-value"""
        pi = 3.1415926536
        e = 2.7182818285
        z = self.z_score(x)
        return (1 / (self.stddev * (2 * pi) ** 0.5)) * e ** (-0.5 * z ** 2)

    def cdf(self, x):
        """Returns the value of the CDF for a given x-value"""
        pi = 3.1415926536
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        erf_part = (z - (z ** 3) / 3
                    + (z ** 5) / 10
                    - (z ** 7) / 42
                    + (z ** 9) / 216)
        erf = (2 / (pi ** 0.5)) * erf_part
        return (1 + erf) / 2
