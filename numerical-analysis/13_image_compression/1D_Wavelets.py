#! /usr/bin/env python
"""
1D Wavelet transform.

Leon Hostetler, Apr. 7, 2017

USAGE: python 1D_Wavelets.py

"""
from __future__ import division, print_function
import numpy as np
import math as math


def phi(t):
    if 0.0 <= t <= 1.0:
        return 1.0
    else:
        return 0.0


def psi(t):
    if 0.0 <= t <= 0.5:
        return 1
    elif 0.5 <= t <= 1.0:
        return -1.0
    else:
        return 0.0


def psi_jk(j, k, t):
    return (2**(j/2))*psi((2**j)*t - k)


# The number of data points. M should be a power of 2
p = 3
M = 2**p

# Construct the A and B matrices
A = np.zeros([M, M], dtype=float)

for j in range(M):
    A[0, j] = (1/np.sqrt(M))*phi((j + 0.5)/M)

for i in range(1, M):
    for j in range(M):
        index1 = math.floor(math.log(i, 2))
        index2 = i - 2**index1
        A[i, j] = (1/np.sqrt(M))*psi_jk(index1, index2, (j + 0.5)/M)


print("\nA = ")
print(A)
print("\nA*A^T = ")
print(np.dot(A, A.T))
