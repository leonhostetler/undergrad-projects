#! /usr/bin/env python
"""
Solves a matrix equation of the form Ax = b
for b, where A is a square matrix. This method includes complete
pivoting (rows and columns).

Leon Hostetler, Jan. 21, 2017

USAGE: python matrix_complete_pivoting.py

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


def solve_complete_pivoting(A, b):
    mat = A.copy()  # Copy passed arrays since they are mutable
    vec = b.copy()
    n = len(b)
    solnswap = np.arange(n)  # Matrix storing the indices of the solution vector
    for i in range(0, n-1):

        # Return index (as tuple) of largest element in submatrix
        ind = np.unravel_index(np.absolute(mat[i:, i:]).argmax(), mat[i:, i:].shape)

        # Swap the rows with indices i and p
        for j in range(0, n):
            mat[i, j], mat[ind[0]+i, j] = mat[ind[0]+i, j], mat[i, j]

        # Swap elements in b-vector as well
        vec[i], vec[ind[0]+i] = vec[ind[0]+i], vec[i]

        # Swap the columns with indices i and c
        for j in range(0, n):
            mat[j, i], mat[j, ind[1]+i] = mat[j, ind[1]+i], mat[j, i]

        # Swap the indices in the solution vector
        solnswap[i], solnswap[ind[1]+i] = solnswap[ind[1]+i], solnswap[i]

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

    # Reorder the solution vector to its original order
    solncopy = solution.copy()
    for i in range(n):
        solution[i] = solncopy[np.argwhere(solnswap == i)[0]]

    return solution

#
#  Output the results
#
soln = solve_complete_pivoting(A, b)
print("Your solution is:\n", soln)
print("\nYour residual vector is:")
print(np.absolute(b - np.dot(A, soln)))
