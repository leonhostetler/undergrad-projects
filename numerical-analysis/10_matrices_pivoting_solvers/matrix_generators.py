#
#  matrix_generators.py i
#
#  Leon Hostetler
#  Jan. 21, 2017
#
#! /usr/bin/env python
"""
Includes several different matrix generators (including
random matrices). These functions can be included in other programs where
random matrices are needed.

Leon Hostetler, Jan. 21, 2017

USAGE: python matrix_generators.py

"""
from __future__ import division, print_function
import numpy as np
import random as rand


# Returns a matrix of size N filled with random integers
# For a 10x10 matrix, the condition number is about
# 250, but it varies a lot from matrix to matrix


def random_integers(N):
    return np.random.randint(-1e4, high=1e4, size=(N, N))


# Returns a matrix of size N filled with random floats between 0 and 1
# For a 10x10 matrix, the condition number is on the
# order of 1e3.


def random_floats(N):
    return np.random.rand(N, N)


# Create a Hilbert matrix of size N
# For a 10x10 matrix, the condition number is 1.602e13
def hilbert_matrix(N):
    mat = np.zeros([N, N])
    for i in range(0, N):
        for j in range(0, N):
            mat[i, j] = 1/(i+j+1)

    return mat


# Returns a random ill-conditioned matrix of size N
# For a 10x10 matrix, the condition number is on the
# order of 1e3.


def random_ill(N):
    eps = 1e-7

    # Random angle for the rotation matrix
    x = rand.uniform(-np.pi, np.pi)

    # This is the base rotation matrix
    q = np.array([[np.cos(x), -np.sin(x)],
                 [np.sin(x), np.cos(x)]])

    # Construct the Q matrix
    Q = np.zeros((N, N))    # First fill it with zeros
    for i in range(N):      # Fill diagonal with 1's
        Q[i, i] = 1
    for i in range(2):      # Replace the top corner with the rotation matrix
        for j in range(2):
            Q[i, j] = q[i, j]

    # Construct the center matrix of random numbers
    D = np.random.rand(N, N)
    for i in range(N):      # Replace the diagonal elements by small numbers
        D[i,i] = rand.uniform(-1e-7, 1e-7)

    # Do the multiplication
    A = np.dot(np.dot(Q, D), Q.transpose())

    return A

# Returns a random ill-conditioned matrix of size N
# For a 10x10 matrix, the condition number is on the
# order of 1e3. Uses the same process as random_ill()
# but instead of multiplying by a single rotation matrix
# and its transpose, it uses 10 rotation matrices and
# their transposes.


def random_very_ill(N):
    eps = 1e-7
    n = 10

    # Construct the center matrix of random numbers
    D = np.random.rand(N, N)
    for i in range(N):  # Replace the diagonal elements by small numbers
        D[i, i] = rand.uniform(-1e-7, 1e-7)

    for k in range(n):

        # Random angle for the rotation matrix
        x = rand.uniform(-np.pi, np.pi)

        # This is the base rotation matrix
        q = np.array([[np.cos(x), -np.sin(x)],
                      [np.sin(x), np.cos(x)]])

        # Construct the Q matrix
        Q = np.zeros((N, N))  # First fill it with zeros
        for i in range(N):  # Fill diagonal with 1's
            Q[i, i] = 1
        for i in range(2):  # Replace the top corner with the rotation matrix
            for j in range(2):
                Q[i, j] = q[i, j]

        # Do the multiplication
        D = np.dot(np.dot(Q, D), Q.transpose())

    return D

# Creates an ill-conditioned matrix by starting with an
# N x N matrix with random floats, then replacing the last
# row by the row before it to make the matrix singular. It
# then adds a very small number to one element in the last
# row, so the matrix becomes almost singular.
# For a 10x10 matrix, the condition number is about 2,000,000.


def random_basic_ill(N):
    mat = np.random.rand(N, N)
    for k in range(N):  # Make the last row same as the row before
        mat[N-1, k] = mat[N-2, k]

    mat[N-1, N-1] += 0.0001  # Change one entry by a little bit

    return mat


#
# Compute condition numbers
#

runs = 100000
total = 0
for m in range(runs):
    A = random_basic_ill(10)
    condA = np.linalg.cond(A)
    total += condA

print()
print(total/runs)
