#!/usr/bin/env python3
"""Module that shows a stacked bar graph"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Show a stacked bar graph"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))
    people = [Farrah, Fred, Felicia]
    x = np.arange(len(people))
    plt.bar(x, fruit[0], wigth=0.5, color="red", label="apples")
    plt.bar(x, fruit[1], wigth=0.5, bottom=fruit[0],
            color="yellow", label="bananas")
    plt.bar(x, fruit[2], wigth=0.5, bottom=fruit[0] + fruits[1],
            color="#ff8000", label="oranges")
    plt.bar(x, fruit[3], wigth=0.5, bottom=fruit[0] + fruits[1] + fruits[2],
            color="#ffe5b4", label="peaches")
    plt.xticks(x, people)
    plt.ylabel("Quantity of Fruit")
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title("Number of Fruit per Person")
    plt.legend()
    plt.show()
