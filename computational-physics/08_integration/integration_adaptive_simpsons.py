#! /usr/bin/env python
"""
Numerically approximates the area under the curve
of a function f(x) using the adaptive Simpson's method of integration.

Leon Hostetler, Feb. 24, 2017

USAGE: python itegration_adaptive_simpsons.py
"""

from __future__ import division, print_function
import numpy as np


a = 0.0                         # Lower integration limit
b = 1.0                        # Upper integration limit

Tol = 1e-6                  # Error tolerance


def f(x):
    """
    Define the function to be integrated.
    """
    return np.sin(np.sqrt(100*x))**2


N = 1  # One integration slice is actually two slices
error = 1.0


w = (b-a)/N                         # Width of each slice
I0 = (w/6)*(f(a) + 4*f((b-a)/2) + f(b))     # Area of first and last slice
print("N = ", N, ", I = ", I0, sep="")


while error > Tol:

    N *= 2
    w = (b-a)/N                         # Width of each slice

    I = 0.5*I0
    for i in range(1, N, 2):
        I += -f(a + w*i)*w/3
    for i in range(0, N):
        I += (2/3)*f(a + w*(i + 1/2))*w

    error = abs(I - I0)/15

    I0 = I
    print("N = ", N, ", I = ", I, ", Error = ", error, sep="")




