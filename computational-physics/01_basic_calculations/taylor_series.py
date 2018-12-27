#! /usr/bin/env python
"""
A basic program for evaluating the exponential function
at a point x, by using the partial sum of its Taylor series.

Leon Hostetler, Feb. 16, 2017

USAGE: python taylor_series.py
"""

from __future__ import division, print_function
import numpy as np
import math as math

# Input
N = 20
x = int(raw_input("Enter an integer for x: "))


# Partial sum
def S(x, N):
    f = np.array([(1/np.math.factorial(k))*(x**k) for k in range(0, N + 1)])
    return f.sum()


# Print the results
print('By the partial sum of the Taylor series, exp(', x, ') = ' + str(S(x, N)), sep="")
print('The value of exp(', x, ') as provided by the math module is: ' + str(math.exp(x)), sep="")
