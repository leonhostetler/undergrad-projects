#! /usr/bin/env python
"""
2D Wavelet transform.

Leon Hostetler, Apr. 8, 2017

USAGE: python 2D_Wavelets.py

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
# Use low p. E.g. p = 5 means A will be a 2^(2p) = 1024 x 1024 matrix
p = 3
M = 2**p

X00_list = []  # Forms the first row of A
for n1 in range(M):
    for n2 in range(M):
        ti = (n1 + 0.5)/M
        tj = (n2 + 0.5)/M
        X00_list.append((1 / M) * phi(ti) * phi(tj))

#print(X00_list)


X0j2k2_array = []  # Forms the next set of rows of A
listoflists1 = []
for j2 in range(p):
    for k2 in range(2**j2):
        newlist = []
        for n1 in range(M):
            for n2 in range(M):
                ti = (n1 + 0.5) / M
                tj = (n2 + 0.5) / M
                newlist.append((1 / M) * phi(ti) * psi_jk(j2, k2, tj))
        listoflists1.append(newlist)

X0j2k2_array = np.vstack(listoflists1)
#print(X0j2k2_array)


Xj1k10_array = []  # Forms the next set of rows of A
listoflists2 = []
for j1 in range(p):
    for k1 in range(2**j1):
        newlist = []
        for n1 in range(M):
            for n2 in range(M):
                ti = (n1 + 0.5) / M
                tj = (n2 + 0.5) / M
                newlist.append((1 / M) * phi(tj) * psi_jk(j1, k1, ti))
        listoflists2.append(newlist)

Xj1k10_array = np.vstack(listoflists2)
#print(Xj1k10_array)


Xj1k1j2k2_array = []  # Forms the rest of the rows of A
listoflists3 = []
for j1 in range(p):
    for k1 in range(2**j1):
        for j2 in range(p):
            for k2 in range(2**j2):
                newlist = []
                for n1 in range(M):
                    for n2 in range(M):
                        ti = (n1 + 0.5) / M
                        tj = (n2 + 0.5) / M
                        newlist.append((1 / M) * psi_jk(j1, k1, ti) * psi_jk(j2, k2, tj))
                listoflists3.append(newlist)

Xj1k1j2k2_array = np.vstack(listoflists3)
#print(Xj1k1j2k2_array)


# Stack them all together to form A
A = np.vstack([X00_list, X0j2k2_array, Xj1k10_array, Xj1k1j2k2_array])

print("\nA = ")
print(A)
print("\nA*A^T = ")
print(np.dot(A, A.T))
