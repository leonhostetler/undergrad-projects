#! /usr/bin/env python
"""

This program gives the partial sum of a Taylor series and compares with the 
actual function being approximated by the Taylor series.

Leon Hostetler, Jan. 14, 2017

USAGE: python eval_partial_sum.py

"""
from __future__ import division, print_function

import numpy as np

# Enter your summation limits here and the value of x at which you
# want the Taylor series evaluated.
lower = 0
upper = 8
x = -np.pi

# Enter the function you're approximating here
truevalue = np.cos(x) - 3.0*np.sin(x)


#
# Enter the summand here. Your variable is x and your summation index is k
#


def summand(k):
    return (1/np.math.factorial(2*k)-(3.0*x)/np.math.factorial(2*k+1))*(x**(2*k))*((-1)**k)


def partial_sum(a, b):  # This is the function that sums the series
    f = np.array([summand(k) for k in range(a, b+1)])
    return f.sum()

#
# Print the results to the console
#
print('Your partial sum is: ' + str(partial_sum(lower, upper)))
print('Your error is: ' + str(np.absolute(truevalue-partial_sum(lower, upper))))
