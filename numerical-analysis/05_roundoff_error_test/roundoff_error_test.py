#! /usr/bin/env python
"""
Test the roundoff error. Checks if x == x + eps for smaller and smaller
values of eps. Prints "FAILURE" when the system recognizes the two as
being the same.

Leon Hostetler, Feb. 2017

USAGE: python roundoff_error_test.py

"""
from __future__ import division, print_function

x = 1.0
eps = 1.0
for i in range(1, 50):

    if x == x + eps:
        print("FAILURE: i = ", i, ", x = ", x, ", eps = ", eps,  sep="")
        break
    else:
        print("SUCCESS: i = ", i, ", x = ", x, ", eps = ", eps, sep="")
    eps = eps/10.0

