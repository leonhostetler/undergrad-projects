#! /usr/bin/env python
"""
Numerically approximate the area under the curve
of a function f(x) using the trapezoidal method of integration.

Leon Hostetler, Feb. 24, 2017

USAGE: integrate_trapezoidal.py
"""

from __future__ import division, print_function

N = 10                          # Number of trapezoids to use
a = 0.0                         # Lower integration limit
b = 10.0                        # Upper integration limit


def f(x):
    """
    Define the function to be integrated.
    """
    return x**4


w = (b-a)/N                     # Width of each trapezoid
s = 0.5*f(a)*w + 0.5*f(b)*w     # Area of first and last trapezoids

for i in range(1, N):           # Area of rest of trapezoids
    s += f(a + i*w)*w

print(s)
