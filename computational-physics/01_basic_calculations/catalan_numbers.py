#! /usr/bin/env python
"""
Compute the Catalan numbers less than 10 billion.

Leon Hostetler, Jan. 28, 2017

USAGE: catalan_numbers.py
"""

from __future__ import division, print_function

# Main body of program

limit = 10000000000     # Print all Catalan numbers less than this
C, n = 1, 0             # Catalan number and its index
print("C_0 = 1")        # Print the first one separately

while C <= limit:       # Loop through and print Catalan numbers
    C = int(((4*n + 2)/(n + 2))*C)
    n += 1
    if C >= limit:      # Final one is greater than the limit unless you break out of the loop
        break
    print("C_", n, " = ", C, sep="")
