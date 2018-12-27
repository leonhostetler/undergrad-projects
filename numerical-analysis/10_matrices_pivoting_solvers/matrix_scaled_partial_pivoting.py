#! /usr/bin/env python
"""
Solves a matrix equation of the form Ax = b
for b, where A is a square matrix. This method includes scaled partial
pivoting.

Leon Hostetler, Jan. 20, 2017

USAGE: python matrx_scaled_partial_pivoting.py

"""
from __future__ import division, print_function
import sys
import numpy as np

#
#  Enter your A and b here
#

A = np.array([[1, 1/2, 1/3, 1/4],
              [1/2, 1/3, 1/4, 1/5],
              [1/3, 1/4, 1/5, 1/6],
              [1/4, 1/5, 1/6, 1/7]], dtype=float)   # Enter your matrix

b = np.array([0, 0, 0, 1], dtype=float)     # Enter your b-vector

epsilon = 1e-18

#
#  This function solves the linear system
#


def solve_scaled_partial_pivoting(mat, vec):
    mat = A.copy()  # Copy passed arrays since they are mutable
    vec = b.copy()
    n = len(vec)

    # Create a vector containing the largest element of each row of A
    scale = np.zeros(n)
    for i in range(n):
        scale[i] = np.absolute(mat[i, :]).max()

    for i in range(0, n-1):

        # Identify the row p containing the largest scaled element in the subcolumn
        p = np.absolute(mat[i:, i] / scale[i:]).argmax() + i

        # Swap the rows with indices i and p
        for j in range(n):
            mat[i, j], mat[p, j] = mat[p, j], mat[i, j]

        # Swap elements in b and scale vectors as well
        vec[i], vec[p] = vec[p], vec[i]
        scale[i], scale[p] = scale[p], scale[i]

        # Eliminate all the values under the pivot positions
        for j in range(i+1, n):         # For each element below the pivot position
            m = mat[j, i]/mat[i, i]     # Compute the scale factor
            for q in range(0, n):       # Row op: R_j = R_j - m*R_i
                mat[j, q] = mat[j, q] - m*mat[i, q]
            vec[j] = vec[j] - m*vec[i]

    if np.absolute(mat[n-1, n-1]) < epsilon:
        sys.exit('No unique solution exists!')

    # Here we start backward substitution
    solution = np.zeros(n)
    solution[n-1] = vec[n-1]/mat[n-1, n-1]
    for i in range(n-2, -1, -1):
        total = 0
        for j in range(i+1, n):
            total += mat[i, j]*solution[j]
        solution[i] = (vec[i] - total)/mat[i, i]

    return solution

#
#  Output the results
#
soln = solve_scaled_partial_pivoting(A, b)
print("Your solution is:\n", soln)
print("\nYour residual vector is:")
print(np.absolute(b - np.dot(A, soln)))
