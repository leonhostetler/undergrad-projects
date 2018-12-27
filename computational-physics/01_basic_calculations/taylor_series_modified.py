#! /usr/bin/env python
"""
A better program for evaluating the exponential function
at a point x, by using the partial sum of its Taylor series.

When x < 0, this program uses 1/S(-x, N) (where S(x, N) is the partial sum of the Taylor
series) to approximate exp(x) with a much better relative error.

Leon Hostetler, Feb. 16, 2017

USAGE: python taylor_series_modified.py
"""

from __future__ import division, print_function
import numpy as np
import math as math


# Input
N = 20
x = int(raw_input("Enter an integer for x: "))


# Partial sum
def S(x, N):
    if x < 0:
        f = np.array([(1/np.math.factorial(k))*((-x)**k) for k in range(0, N+1)])
        return 1/f.sum()
    else:
        f = np.array([(1/np.math.factorial(k))*(x**k) for k in range(0, N+1)])
        return f.sum()


# Print the results
print('By the partial sum of the Taylor series, exp(', x, ') = ' + str(S(x, N)), sep="")
print('The value of exp(', x, ') as provided by the math module is: ' + str(math.exp(x)), sep="")
