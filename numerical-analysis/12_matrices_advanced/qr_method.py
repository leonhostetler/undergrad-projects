#! /usr/bin/env python
"""
Here we start with an upper Hessenberg matrix and convert it to an
upper triangular matrix using Givens rotations. The result is the
QR factorization of the matrix.

Leon Hostetler, Mar. 7, 2017

USAGE: python qr_method.py

"""
from __future__ import division, print_function
import numpy as np

qrTol = 1e-15  # Error tolerance for QR

# Start with a symmetric matrix
n = 3  # Size of matrix
A = np.array([(1, 2, 0),
              (2, 1, 1),
              (0, 1, 0)])

print("A = \n", A)

#
# The first step is to use Givens rotations to zero the elements in the
# lower diagonal band.
#

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


H = np.copy(A)
print("\nHessenberg = \n", H)


# Apply Givens rotation matrices to convert the upper Hessenberg matrix
# to a triangular matrix R.
#       G[n-1]...G[3]G[2]G[1]H = R
# Then
#       Q = (G[n-1]...G[3]G[2]G[1])^T
def qr_by_givens(H):
    Qt = np.identity(n)  # The transpose of Q
    R = H
    for i in range(n-1):  # For all the lower diagonal elements
        G = givens(i+1, i, R)
        R, Qt = np.dot(G, R), np.dot(G, Qt)

    Q = Qt.T  # Q is the transpose of Qt

    return Q, R

# The QR method is used to transform a symmetric matrix to a diagonal
# matrix using similarity transformations so the eigenvalues and
# eigenvectors can be obtained.

k = 0
U = np.identity(n)
flag = False
while flag is False:
    qr = qr_by_givens(H)
    Q = qr[0]
    R = qr[1]

    H = np.dot(R, Q)
    U = np.dot(U, Q)  # Save the eigenvectors

    k += 1

    # Check if all the off-diagonal elements are ~0
    flag = True
    for i in range(n):
        for j in range(n):
            if i != j and abs(H[i, j]) > qrTol:
                flag = False
                break

print("\nIterations = ", k)
print("\nH is now: \n", H)
print("\nThe eigenvalues of H are: ")
print(np.diagonal(H))

# The eigenvectors are the columns of
#   U = Q_n...Q_2Q_1
print("\nThe eigenvectors are:")
print(U)


