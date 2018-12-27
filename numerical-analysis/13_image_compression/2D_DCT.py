#! /usr/bin/env python
"""
2D Discrete Cosine Transform.

Leon Hostetler, Apr. 14, 2017

USAGE: python 2D_DCT.py

"""
from __future__ import division, print_function
import numpy as np
import math as math

# The size of the input matrix
N = 5
points = N**2

# Construct the A and B matrices
A = np.zeros([points, points], dtype=float)

for i in range(points):
    for j in range(points):

        k1 = math.floor(i/N)
        k2 = i % N
        n1 = math.floor(j/N)
        n2 = j % N

        if k1 == 0:
            alpha1 = 1/np.sqrt(N)
        else:
            alpha1 = np.sqrt(2/N)
        if k2 == 0:
            alpha2 = 1/np.sqrt(N)
        else:
            alpha2 = np.sqrt(2/N)
        alphas = alpha1*alpha2

        A[i, j] = alphas*np.cos(k1*np.pi*(n1+0.5)/N)*np.cos(k2*np.pi*(n2+0.5)/N)

print("\nA = ")
print(A)
print("\nA*A^T = ")
print(np.dot(A, A.T))
