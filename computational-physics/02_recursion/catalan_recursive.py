#! /usr/bin/env python
"""
Compute a Catalan number recursively.

Leon Hostetler, Jan. 31, 2017

USAGE: catalan_recursive.py
"""

from __future__ import division, print_function

# Main body of program

n = int(raw_input("Enter n to get Catalan number C_n: "))


def catalan(i):
    """
    This function returns C_n, the Catalan number,
    calculated using recursion.
    """
    if i == 0:
        return 1
    else:
        return int(((4*i - 2)/(i + 1))*catalan(i-1))


print("\nC_", n, " = ", catalan(n), sep="")
