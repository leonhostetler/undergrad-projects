#! /usr/bin/env python
"""
This program gives the partial sum of a Taylor series.

Leon Hostetler, Jan. 13, 2017

USAGE: python simple_partial_sum.py

"""
from __future__ import division, print_function
import numpy as np

# Enter your summation limits here and the value of x at which you
# want the Taylor series evaluated.
lower = 0
upper = 7
x = np.pi

# Enter the summand here. Your variable is x and your summation index is k
def Summand(k):
    return (1/np.math.factorial(2*k)-(3*x)/np.math.factorial(2*k+1))*x**(2*k)*(-1)**k

# This is the function that sums the series
def PartialSum(a, b):
    f = np.array([Summand(k) for k in range(a, b+1)])
    return f.sum()

# This prints the results to the console
print('Your partial sum is: ' + str(PartialSum(lower,upper)))
