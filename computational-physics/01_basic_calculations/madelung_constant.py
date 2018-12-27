#! /usr/bin/env python
"""
Approximate the Madelung constant for NaCl. The procedure is as follows:

    We consider a sodium atom at the origin (0,0,0) of a cube of side length 2L.
    Each point on the integer lattice is occupied by alternating sodium and
    chlorine atoms. Then we calculate the total potential at the origin due to every
    atom in the cube.

Leon Hostetler, Jan. 28, 2017

USAGE: madelung_constant.py
"""

from __future__ import division, print_function
import numpy as np

# Main body of program

L = 200  # Size of the NaCl cube

M = 0
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if i == 0 and j == 0 and k == 0:    # Skip (0,0,0)
                continue
            if (i + j + k) % 2 == 0:
                M += (1/np.sqrt(i**2 + j**2 + k**2))
            else:
                M += -(1/np.sqrt(i**2 + j**2 + k**2))

print("\nThe cube side length used is 2L = ", 2*L)
print("Total atoms considered: ", (2*L+1)**3)
print("Our approximation of the Madelung constant is M = ", M)
