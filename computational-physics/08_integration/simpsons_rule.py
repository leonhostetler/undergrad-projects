#! /usr/bin/env python
"""
Numerically approximate the integral of x^4 - 2x + 1 from
x = 0 to x = 2 using Simpson's Rule.

Leon Hostetler, Feb. 25, 2017

USAGE: python simpsons_rule.py
"""

from __future__ import division, print_function

N = 1000    # Number of trapezoids to use
a = 0.0     # Lower integration limit
b = 2.0     # Upper integration limit


def f(x):
    """
    This defines the integrand of the Gaussian error function E(x).
    """
    return x**4 - 2*x + 1


# The number of slices must be even for Simpson's Rule to be accurate
if N % 2 != 0:
    N += 1
    print("Number of slices was odd so 1 was added to N.")

w = (b-a)/N                         # Width of each slice
s = (1/3)*f(a)*w + (1/3)*f(b)*w     # Area of first and last slice

for i in range(1, N, 2):            # Odd terms
    s += f(a + i*w)*w*(4/3)

for i in range(2, N, 2):            # Even terms
    s += f(a + i*w)*w*(2/3)

print("\nWith N = ", N, ", Simpson's Rule gives us ", s, ".", sep="")
print("\nThe actual value is 4.4, and our fractional error is ", abs(s - 4.4)/4.4, ".", sep="")
