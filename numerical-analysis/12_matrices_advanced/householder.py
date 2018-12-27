#! /usr/bin/env python
"""
This program uses Householder transformations to transform a square matrix into
an upper Hessenberg matrix using similarity transformations.

Leon Hostetler, Mar. 5, 2017

USAGE: python householder.py

NOTE: Start with a symmetric matrix. You don't need to start with a symmetric matrix to convert a matrix to upper Hessenberg form using Householder transformations, but you need
a symmetric matrix for the QR algorithm that follows it. If you convert a
symmetric matrix to upper Hessenberg form using Householder transformations,
it will actually end up being a tridiagonal matrix.

"""
from __future__ import division, print_function
import numpy as np

n = 3  # Size of matrix
A = np.array([(1, 2, 3),
              (2, 5, 6),
              (3, 6, 9)])

print("A = ", A)

for k in range(1, n-1):
    # Generate the Householder reflector P_k

    s = 0.0
    for j in range(k+1, n+1):
        s += A[j-1, k-1]**2
    alpha = -np.sign(A[k, k-1])*np.sqrt(s)
    #print("alpha = ", alpha)

    r = np.sqrt(0.5*alpha**2 - 0.5*alpha*A[k, k-1])
    #print("r = ", r)

    # Create the w vector
    w = np.zeros([n])
    w[k] = (A[k, k-1] - alpha)/(2*r)

    #print(w)

    for j in range(k+2, n+1):
        w[j-1] = A[j-1, k-1]/(2*r)

    #print("w = ", w)

    P = np.identity(n) - 2*np.outer(w, w.T)
    #print("P = ", P)

    # Apply the similarity transformation
    A = np.dot(A, P)
    A = np.dot(P, A)

print("Hessenberg A = ", A)
