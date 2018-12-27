#! /usr/bin/env python
"""
Numerically approximates the area under the curve
of a function f(x) using the adaptive trapezoidal method of integration.

Leon Hostetler, Feb. 24, 2017

USAGE: python integration_adaptive_trap.py
"""

from __future__ import division, print_function
import numpy as np


a = 0.0                        # Lower integration limit
b = 1.0                        # Upper integration limit
Tol = 1e-6                     # Error tolerance


def f(x):
    """
    Define the function to be integrated.
    """
    return np.sin(np.sqrt(100*x))**2

error = 1
N = 1

# I0 is the approximation with a single trapezoid
I0 = (f(a) + f(b))*(b-a)*0.5
print("N = ", N, ", I = ", I0, sep="")

while error > Tol:

    N *= 2
    w = (b - a) / N  # Width of each trapezoid

    I = 0.5*I0
    for i in range(1, N, 2):
        I += f(a + i*w)*w

    error = abs(I - I0)/3

    I0 = I
    print("N = ", N, ", I = ", I, ", Error = ", error, sep="")



