#! /usr/bin/env python
"""
Compute the greatest common divisor of two nonnegative integers using
a recursive user-defined function.

Leon Hostetler, Feb. 2, 2017

USAGE: gcd.py
"""

from __future__ import division, print_function

# Main body of program

m = int(raw_input("Enter your first nonnegative integer: "))
n = int(raw_input("Enter your second nonnegative integer: "))


def gcd(a, b):
    """
    This function computes the greatest common divisor of m and n.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print("\nThe greatest common divisor of ", m, " and ", n, " is: ", gcd(m, n))
