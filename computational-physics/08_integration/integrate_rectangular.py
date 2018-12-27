#! /usr/bin/env python
"""
Numerically approximate the area under the curve
of a function f(x) by dividing the area into rectangles.

Leon Hostetler, Feb. 24, 2017

USAGE: integrate_rectangular.py
"""

from __future__ import division, print_function


N = 10              # Number of rectangles to use
a = 0.0             # Lower integration limit
b = 10.0            # Upper integration limit



def f(x):
    """
    Define the function to be integrated.
    """
    return x**4


w = (b-a)/N         # Width of each rectangle
s = 0.0             # Sum the area of all the rectangles

for i in range(N):
    s += f(a + w/2 + i*w)*w

print(s)
