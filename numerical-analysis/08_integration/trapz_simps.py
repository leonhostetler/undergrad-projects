#! /usr/bin/env python
"""
Uses the composite trapezoid and simpson rules to
perform numerical integration.

Leon Hostetler, Mar. 2017

USAGE: python trapz_simps.py

"""
from __future__ import division, print_function
import numpy as np


def integrate_trapz(f, lower, upper, N=1000):
    """
    Integrate the function from lower to upper using
    trapezoidal integration.

    Takes in the function, the lower and upper limits of integration,
    and the number of trapezoidal slices to use.
    """
    a = lower           # Lower integration limit
    b = upper           # Upper integration limit
    w = (b - a) / N     # Width of each trapezoid

    # Area of first and last trapezoids
    I = 0.5 * f(a) * w + 0.5 * f(b) * w

    # Area of rest of trapezoids
    for i in range(1, N):
        I += f(a + i * w) * w

    return I, N


def integrate_simpson(f, lower, upper, N=1000):
    """
    Integrate the function from lower to upper using
    simpson integration.

    Takes in the function, the lower and upper limits of integration,
    and the number of slices to use.
    """
    a = lower           # Lower integration limit
    b = upper           # Upper integration limit
    w = (b - a) / N     # Width of each trapezoid

    if N % 2 != 0:
        N += 1
        print("Number of slices was odd so 1 was added to N.")

    I = (1 / 3) * f(a) * w + (1 / 3) * f(b) * w  # Area of first and last trapezoids

    for i in range(1, N, 2):  # Odd terms
        I += f(a + i * w) * w * (4 / 3)

    for i in range(2, N, 2):  # Even terms
        I += f(a + i * w) * w * (2 / 3)

    return I, N


def f(x):
    fx = np.exp(-x**2)
    #fx = x**3
    #fx = x
    return fx

#
# MAIN
#

# Trapezoid method is exact for f(x) = x if N = 2 and Simpson rule
# is exact for both f(x) = x and f(x) = x^3 if N = 2. If N is large,
# we get a very small amount of numerical error for these.
#

trap = integrate_trapz(f, 0, 1, N=10)
simp = integrate_simpson(f, 0, 1, N=10)

print("\nThe trapezoid rule gives: ", trap, sep="")
print("The Simpson rule gives: ", simp, sep="")
