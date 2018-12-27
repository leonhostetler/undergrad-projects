#! /usr/bin/env python
"""
This program uses Householder transformations to transform a square matrix into
an upper Hessenberg matrix using similarity transformations.

Leon Hostetler, Mar. 9, 2017

USAGE: python householder_qr.py

"""
from __future__ import division, print_function
import numpy as np

####################################
# Create the matrix
# Since we need a symmetric matrix for the QR method, we need to
# start with a symmetric matrix.
####################################

n = 4  # Size of matrix
A = np.array([(1, 2, 3, 4),
              (2, 5, 6, 7),
              (3, 6, 9, 10),
              (4, 7, 10, 11)], dtype=float)

print("A = \n", A)

####################################
# Householder section
# Here we convert the matrix to an upper Hessenberg matrix or
# a symmetric matrix into a tridiagonal matrix.
####################################

PTOTAL = np.identity(n)

for k in range(1, n-1):
    s = 0.0
    for j in range(k+1, n+1):
        s += A[j-1, k-1]**2
    alpha = -np.sign(A[k, k-1])*np.sqrt(s)

    r = np.sqrt(0.5*alpha**2 - 0.5*alpha*A[k, k-1])

    # Create the w vector
    w = np.zeros([n])
    w[k] = (A[k, k-1] - alpha)/(2*r)

    for j in range(k+2, n+1):
        w[j-1] = A[j-1, k-1]/(2*r)

    # The Householder reflector P_k
    P = np.identity(n) - 2*np.outer(w, w.T)

    # Apply the similarity transformation
    A = np.dot(P, np.dot(A, P))

    # Save the eigenvectors
    #   U = P_n*...*P_2*P_1*I
    PTOTAL = np.dot(PTOTAL, P)


####################################
# QR section
# The QR method is used to transform a symmetric matrix to a diagonal
# matrix using similarity transformations so the eigenvalues and
# eigenvectors can be obtained.
####################################

qrTol = 1e-15  # Error tolerance for QR


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


#H = np.copy(A)
H = A
print("\nHessenberg = \n", H)


def qr_by_givens(H):
    # Apply Givens rotation matrices to convert the upper Hessenberg matrix
    # to a triangular matrix R.
    #       G[n-1]...G[3]G[2]G[1]H = R
    # Then
    #       Q = (G[n-1]...G[3]G[2]G[1])^T
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
QTOTAL = np.identity(n)
#QTOTAL = PTOTAL
flag = False
while flag is False:
    qr = qr_by_givens(H)  # Factor H = QR
    #qr = np.linalg.qr(H)
    Q = qr[0]
    R = qr[1]

    H = np.dot(R, Q)
    QTOTAL = np.dot(QTOTAL, Q)  # Save the eigenvectors

    k += 1

    # Check if all the off-diagonal elements are ~0
    flag = True
    for i in range(n):
        for j in range(n):
            if i != j and abs(H[i, j]) > qrTol:
                flag = False
                break


####################################
# RESULTS
####################################

print("\nQR Iterations = ", k)
print("\nH is now: \n", H)
print("\nThe eigenvalues of H are: ")
print(np.diagonal(H))

# The eigenvectors are the columns of
U = np.dot(PTOTAL, QTOTAL)
print("\nThe eigenvectors are the columns of:")
print(U)




