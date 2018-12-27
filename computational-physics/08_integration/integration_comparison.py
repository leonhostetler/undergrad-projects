#! /usr/bin/env python
"""
Numerically approximate the area under the curve
of a function f(x) using different integration techniques.

Leon Hostetler, Feb. 24, 2017

USAGE: python integration_comparison.py
"""

from __future__ import division, print_function
import numpy as np


def f(x):
    """
    Define the function to be integrated.
    """
    return x**5 - 13*x**4 + 47*x**3 - 59*x**2 + 24*x
    #return np.absolute(x)
    #return 3


def integrate_rectangular(a, b, N):
    """
    The function integrates f(x) using using rectangles. The parameters
    passed, in order, are the lower limit of integration, the upper
    limit, and the number of rectangles.
    """
    w = (b - a) / N  # Width of each rectangle
    s = 0.0  # Sum the area of all the rectangles

    for i in range(N):
        s += f(a + w / 2 + i * w) * w

    return s


def integrate_trapezoidal(a, b, N):
    """
    The function integrates f(x) using using trapezoids. The parameters
    passed, in order, are the lower limit of integration, the upper
    limit, and the number of trapezoids.
    """
    w = (b - a) / N  # Width of each trapezoid
    s = 0.5 * f(a) * w + 0.5 * f(b) * w  # Area of first and last trapezoids

    for i in range(1, N):  # Area of rest of trapezoids
        s += f(a + i * w) * w

    return s


def integrate_simpson(a, b, N):
    """
    The function integrates f(x) using Simpson's Rule. The parameters
    passed, in order, are the lower limit of integration, the upper
    limit, and the number of "slices".
    """
    # The number of slices must be even for Simpson's Rule to be accurate
    if N % 2 != 0:
        N += 1
        print("Number of slices was odd so 1 was added to N.")

    w = (b - a) / N  # Width of each slice
    s = (1 / 3) * f(a) * w + (1 / 3) * f(b) * w  # First and last terms

    for i in range(1, N, 2):  # Odd terms
        s += f(a + i * w) * w * (4 / 3)

    for i in range(2, N, 2):  # Even terms
        s += f(a + i * w) * w * (2 / 3)

    return s


rect = integrate_rectangular(0.0, 10.0, 90)
trap = integrate_trapezoidal(0.0, 10.0, 127)
simp = integrate_simpson(0.0, 10.0, 17)

print(rect)
print(trap)
print(simp)
