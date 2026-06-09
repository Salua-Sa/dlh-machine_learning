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
