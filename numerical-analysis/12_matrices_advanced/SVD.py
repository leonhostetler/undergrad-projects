#! /usr/bin/env python
"""
This program uses Householder transformations to transform a square matrix into
an upper Hessenberg matrix using similarity transformations.

Leon Hostetler, Mar. 7, 2017

USAGE: python SVD.py

"""
from __future__ import division, print_function
import numpy as np


def givens(i, j, mat):
    """
    This function returns an n x n Givens rotation matrix G that will zero
    the A[i, j] element when you multiply G*A.
    """
    n = len(mat)
    G = np.zeros([n, n])        # Initialize rotation matrix as matrix of zeros
    for k in range(n):          # Set diagonal elements to 1
        G[k, k] = 1.0

    d = np.sqrt(mat[j, j]**2 + mat[i, j]**2)
    c = mat[j, j]/d
    s = mat[i, j]/d

    G[j, j] = c
    G[i, j] = -s
    G[i, i] = c
    G[j, i] = s

    return G


def qr_by_givens(mat):
    # Apply Givens rotation matrices to convert the upper Hessenberg matrix
    # to a triangular matrix R.
    #       G[n-1]...G[3]G[2]G[1]H = R
    # Then
    #       Q = (G[n-1]...G[3]G[2]G[1])^T
    n = len(mat)
    Qt = np.identity(n)  # The transpose of Q
    R = mat
    for i in range(n-1):  # For all the lower diagonal elements
        G = givens(i+1, i, R)
        R, Qt = np.dot(G, R), np.dot(G, Qt)
    Q = Qt.T  # Q is the transpose of Qt

    return Q, R


def eig(mat, qrTol):
    """
    Returns the eigenvalues and eigenvectors of a symmetric matrix A using
    the QR method.

    The first part of this function is the Householder section, where we
    convert the symmetric matrix to an upper Hessenberg matrix.
    """

    n = len(mat)

    PTOTAL = np.identity(n)

    for k in range(1, n-1):
        s = 0.0
        for j in range(k+1, n+1):
            s += mat[j-1, k-1]**2
        alpha = -np.sign(mat[k, k-1])*np.sqrt(s)

        r = np.sqrt(0.5*alpha**2 - 0.5*alpha*mat[k, k-1])

        # Create the w vector
        w = np.zeros([n])
        w[k] = (mat[k, k-1] - alpha)/(2*r)

        for j in range(k+2, n+1):
            w[j-1] = mat[j-1, k-1]/(2*r)

        # The Householder reflector P_k
        P = np.identity(n) - 2*np.outer(w, w.T)

        # Apply the similarity transformation
        mat = np.dot(P, np.dot(mat, P))

        # Save the eigenvectors
        #   U = P_n*...*P_2*P_1*I
        PTOTAL = np.dot(PTOTAL, P)

    H = mat

    """
    Here begins the QR section.

    The QR method is used to transform a symmetric matrix to a diagonal
    matrix using similarity transformations so the eigenvalues and
    eigenvectors can be obtained.
    """

    k = 0
    QTOTAL = np.identity(n)
    flag = False
    while flag is False:
        qr = qr_by_givens(H)  # Factor H = QR
        # qr = np.linalg.qr(H)
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

    # The eigenvalues are the diagonal elements of
    D = np.diagonal(H)

    # The eigenvectors are the columns of
    V = np.dot(PTOTAL, QTOTAL)

    return D, V


####################################
# MAIN PART
# Create the matrix
# Since we need a symmetric matrix for the QR method, we need to
# start with a symmetric matrix.
####################################

n = 3
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

# The columns of U are the eigenvectors of A*A^T
U = eig(np.dot(A, A.T), 1e-10)[1]

# The columns of V are the eigenvectors of A^T*A
V = eig(np.dot(A.T, A), 1e-10)[1]

# Sigma is a diagonal matrix whose entries are the eigenvalues of A
eigs = eig(A, 1e-10)[0]
Sigma = np.zeros([N, N])

for i in range(len(eigs)):
    Sigma[i, i] = eigs[i]

print("\nU = \n", U)
print("\nSigma = \n", Sigma)
print("\nV^T = \n", V.T)

print("\nThe product U*Sigma*V^T should be equal to the original matrix A:")
USV = np.dot(U, np.dot(Sigma, V.T))
print(USV)

print("\nThe difference between the two is:")
print(A - USV)











