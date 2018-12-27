#! /usr/bin/env python
"""
Approximate the precisions of Numpy's different
data types by repeatedly dividing 1.0 by 2.0 until and adding it to 1.0
until the result is no longer distinguishable from 1.0.

Leon Hostetler, Feb. 25, 2017

USAGE: floating_point_precision.py
"""

from __future__ import division, print_function
import numpy as np

# Approximate the precision of Numpy's 16-bit floating point number
# by setting x = 1.0 and repeatedly dividing it by 2.0 and adding the
# result to 1.0 until the two are no longer distinguishable.
x = np.float16(1.0)
while x + np.float16(1.0) != np.float16(1.0):
    x /= np.float16(2.0)
print("For float16: ", x)

# Repeat for float32
x = np.float32(1.0)
while x + np.float32(1.0) != np.float32(1.0):
    x /= np.float32(2.0)
print("For float32: ", x)

# Repeat for float64
x = np.float64(1.0)
while x + np.float64(1.0) != np.float64(1.0):
    x /= np.float64(2.0)
print("For float64: ", x)

# Repeat for float128
x = np.float128(1.0)
while x + np.float128(1.0) != np.float128(1.0):
    x /= np.float128(2.0)
print("For float128: ", x)
