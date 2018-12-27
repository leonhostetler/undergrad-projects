#! /usr/bin/env python
"""
Given the 1D discrete Fourier transform
    X = Ax,
and the inverse discrete Fourier transform
    x = BX,
construct the A matrix for some N and verify
that AA^T = I.

Leon Hostetler, Apr. 14, 2017

USAGE: python 1D_DCT.py

"""
from __future__ import division, print_function
import numpy as np

# The size of the DCT matrix
N = 3

# Construct the A and B matrices
A = np.zeros([N, N], dtype=float)
#B = np.zeros([N, N], dtype=float)
for i in range(N):
    for j in range(N):
        if i == 0:
            alpha = np.sqrt(1/N)
        else:
            alpha = np.sqrt(2/N)
        A[i, j] = alpha*np.cos(i*np.pi*(j+0.5)/N)

print("\nA = ")
print(A)
print("\nA*A^T = ")
print(np.dot(A, A.T))
