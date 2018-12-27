#! /usr/bin/env python
"""
Print the first 20 rows of Pascal's triangle.

Leon Hostetler, Jan. 31, 2017

USAGE: pascals_triangle.py
"""

from __future__ import division, print_function

# Main body of program


def binomial(n, k):
    """
    This function computes the binomial n choose k using the formula
    (n(n-1)(n-1)...(n-k+1)) / (1*2*3*...*k)
    """
    if k == 0:
        return 1

    num, denom = 1, 1
    for m in range(n, n-k, -1):     # Compute the numerator
        num *= m
    for m in range(1, k+1):         # Compute the denominator
        denom *= m

    return int(num/denom)


for i in range(20):             # Loop through rows 0 to 20 of Pascal's triangle
    my_list = []                # A list containing the elements of the row
    for j in range(i + 1):      # Loop through each element in the row
        my_list.append(binomial(i, j))
    print(*my_list, sep=', ')   # Print the row with comma separation and no brackets
