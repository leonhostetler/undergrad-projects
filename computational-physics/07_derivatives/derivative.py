#! /usr/bin/env python
"""
Numerically compute the derivative of f(x) = x(x-1) using different
values for the small number delta.

Leon Hostetler, Feb. 21, 2017

USAGE: python derivative.py
"""

from __future__ import division, print_function

# Main body of program


def f(x):
    """
    This function returns the value of f(x) = x(x-1)
    """
    return x*(x-1)


def der(x, delta):
    """
    This function returns the derivative f'(x) at x given a value for delta.
    """
    return (f(x+delta) - f(x))/delta

print("\n The actual value is f'(1) = 1. Following are the numerical approximations.\n")

# Here, we compute f'(1) numerically using different values of
# delta and print the results.
for i in range(2, 20, 2):
    print("f'(1) with delta = ", 10**(-i), " is: ", der(1, 10**(-i)), sep="")
