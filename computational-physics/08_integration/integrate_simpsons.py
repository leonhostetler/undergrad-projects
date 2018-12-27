#! /usr/bin/env python
"""
Numerically approximate the area under the curve
of a function f(x) using simpson's rule.

Leon Hostetler, Feb. 24, 2017

USAGE: python integrate_simpsons.py
"""

from __future__ import division, print_function

N = 10                              # Number of trapezoids to use
a = 0.0                             # Lower integration limit
b = 10.0                            # Upper integration limit


def f(x):
    """
    Define the function to be integrated.
    """
    return x**4

# The number of slices must be even for Simpson's Rule to be accurate
if N % 2 != 0:
    N += 1
    print("Number of slices was odd so 1 was added to N.")


w = (b-a)/N                         # Width of each trapezoid
s = (1/3)*f(a)*w + (1/3)*f(b)*w     # Area of first and last trapezoids

for i in range(1, N, 2):            # Odd terms
    s += f(a + i*w)*w*(4/3)

for i in range(2, N, 2):            # Even terms
    s += f(a + i*w)*w*(2/3)

print(s)
