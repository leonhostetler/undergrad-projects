#! /usr/bin/env python
"""

Leon Hostetler, Mar. 9, 2017

USAGE: python main.py

"""
from __future__ import division, print_function
import numpy as np
import mySVD

####################################
# Create the matrix
####################################

n = 2
N = n**2  # The overall size of the matrix

A = np.zeros([N, N])

p = 1
for j in range(0, n):
    for i in range(0, n):
        d = 0.0
        if i > 0:
            A[p-1, p-2] = -1.0
            d += 1.0
        if i < n-1:
            A[p-1, p] = -1.0
            d += 1.0
        if j > 0:
            A[p-1, p-n-1] = -1.0
            d += 1.0
        if j < n-1:
            A[p-1, p+n-1] = -1.0
            d += 1.0
        A[p-1, p-1] = d
        p += 1


print("\nThe original matrix is:\n", A)

####################################
# Decompose A using a singular value decomposition
####################################

SVD = mySVD.singular_value_decomposition(A, 1e-10)
Ainv = mySVD.pseudoinverse(A, 1e-10)

U = SVD[0]
Sigma = SVD[1]
Vt = SVD[2].T

print("\nU = \n", U)
print("\nSigma = \n", Sigma)
print("\nV^T = \n", Vt)

print("\nThe product U*Sigma*V^T should be equal to the original matrix A:\n")
USV = np.dot(U, np.dot(Sigma, Vt))
print(USV)

print("\nThe difference between the two is:\n")
print(A - USV)


##################################
# Solve Ax = b using the pseudoinverse
##################################

#b = np.zeros([N])
#b[N-1] = 1.0
b = np.array([1, 1, 1, -3])

# The vector w can be anything
w = np.ones([N])

# The solution is
x = np.dot(Ainv, b) + np.dot((np.identity(N) - np.dot(Ainv, A)), w)

print("\nThe pseudoinverse of A is:")
print(Ainv)

print("\nChoose b = \n", b)
print("\nThen x = \n", x)
print("\nCheck that Ax = b. Ax = \n", np.dot(A, x))

#print("\nCheck that A^+AA^+ = A^+:")
#AAinvA = np.dot(Ainv, np.dot(A, Ainv))
#print(AAinvA)

#print("\nCheck that AA^+A = A:")
#AAinvA = np.dot(A, np.dot(Ainv, A))
#print(AAinvA)

#print("\nCheck that AA^+b = b:")
#AAinvb = np.dot(A, np.dot(Ainv, b))
#print(AAinvb)

#print("\nA^+b:")
#print(np.dot(Ainv, b))

#print("\nAA^+:")
#print(np.dot(A, Ainv))

#print("\n(I-A^+A)w:")
#print(np.dot((np.identity(N) - np.dot(Ainv, A)), w))

