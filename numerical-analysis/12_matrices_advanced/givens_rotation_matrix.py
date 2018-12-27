#! /usr/bin/env python
"""
Use Givens rotation matrices to selectively zero out the elements of a matrix.

Leon Hostetler, Mar. 2017

USAGE: python givens-rotation-matrix.py

"""
from __future__ import division, print_function
import numpy as np


n = 3  # Size of matrix

A = np.array([(1, 2, 0),
              (1, 1, 1),
              (2, 1, 0)])

print("A = \n", A)


def givens(i, j, A):
    """
    This function returns an n x n Givens rotation matrix G that will zero
    the A[i, j] element when you multiply G*A.
    """
    G = np.zeros([n, n])        # Initialize rotation matrix as matrix of zeros
    for k in range(n):          # Set diagonal elements to 1
        G[k, k] = 1.0

    d = np.sqrt(A[j, j]**2 + A[i, j]**2)
    c = A[j, j]/d
    s = A[i, j]/d

    G[j, j] = c
    G[i, j] = -s
    G[i, i] = c
    G[j, i] = s

    return G


# Zero out A[1,0] with a Givens rotation matrix
G1 = givens(1, 0, A)
print("\nG1 = \n", G1)
A = np.dot(G1, A)
print("A is now = \n", A)

# Zero out A[2,0] with a Givens rotation matrix
G2 = givens(2, 0, A)
print("G2 = \n", G2)
A = np.dot(G2, A)
print("A is now = \n", A)

# Zero out A[2,1] with a Givens rotation matrix
G3 = givens(2, 1, A)
print("G3 = \n", G3)
A = np.dot(G3, A)
print("A is now = \n", A)
