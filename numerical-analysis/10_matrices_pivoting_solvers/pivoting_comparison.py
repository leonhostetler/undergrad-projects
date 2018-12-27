#! /usr/bin/env python
"""
Compare the performance of the different methods for solving linear systems.

Leon Hostetler, Jan. 20, 2017

USAGE: python pivoting_comparison.py

"""
from __future__ import division, print_function
import sys
import numpy as np
import random as rand

N = 20  # Choose matrix size
epsilon = 1e-20

#
#  Swap rows only when the pivot is zero
#


def solve_basic(A, b):
    mat = A.copy()  # Copy passed arrays since they are mutable
    vec = b.copy()
    n = len(vec)

    for i in range(0, n-1):

        # Swap with row beneath if pivot element is zero
        if np.absolute(mat[i, i]) < epsilon:
            for j in range(0, n):
                mat[i, j], mat[i+1, j] = mat[i+1, j], mat[i, j]

            # Swap elements in b-vector
            vec[i], vec[i+1] = vec[i+1], vec[i]

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
#  Solve using partial pivoting
#


def solve_partial_pivoting(A, b):
    mat = A.copy()  # Copy passed arrays since they are mutable
    vec = b.copy()
    n = len(vec)

    for i in range(0, n-1):

        # Identify the row p containing the largest element in the subcolumn
        p = np.absolute(mat[i:, i]).argmax() + i

        # Swap the rows with indices i and p
        for j in range(0, n):
            mat[i, j], mat[p, j] = mat[p, j], mat[i, j]

        # Swap elements in b-vector as well
        vec[i], vec[p] = vec[p], vec[i]

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
#  Solve using scaled partial pivoting
#


def solve_scaled_partial_pivoting(A, b):
    mat = A.copy()  # Copy passed arrays since they are mutable
    vec = b.copy()
    n = len(vec)

    # Create a vector containing the largest element of each row of A
    scale = np.zeros(n)
    for i in range(n):
        scale[i] = np.absolute(mat[i, :]).max()

    for i in range(0, n-1):

        # Identify the row p containing the largest scaled element in the subcolumn
        p = np.absolute(mat[i:, i]/scale[i:]).argmax() + i

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
#  Solve using complete pivoting
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
# Generate random matrix
#


def generate_matrix(N):
    return np.random.rand(N, N)  # Matrix with random floats

#
# Run the program
#

runs = 1000  # Number of times to run the program

errppwins = 0
errnpwins = 0
errsppwins = 0
errcpwins = 0

resppwins = 0
resnpwins = 0
ressppwins = 0
rescpwins = 0

totalnperr = 0
totalpperr = 0
totalspperr = 0
totalcperr = 0

totalnpres = 0
totalppres = 0
totalsppres = 0
totalcpres = 0

for k in range(runs):
    # Create random matrix
    A = generate_matrix(N)

    # Create an x-vector to compare against later
    x = np.random.rand(N)

    # Compute the b vector
    b = np.dot(A, x)

    # Note: If custom b vector is used instead of the randomly generated one
    # then the direct error printed to the console will be meaningless since
    # b is no longer calculated from x.
    #b = np.zeros(N)
    #b[N-1] = 1

    np_soln = solve_basic(A, b)
    pp_soln = solve_partial_pivoting(A, b)
    spp_soln = solve_scaled_partial_pivoting(A, b)
    cp_soln = solve_complete_pivoting(A, b)

    # By direct error
    np_err = np.absolute(x - np_soln)
    pp_err = np.absolute(x - pp_soln)
    spp_err = np.absolute(x - spp_soln)
    cp_err = np.absolute(x - cp_soln)
    totalnperr += np_err
    totalpperr += pp_err
    totalspperr += spp_err
    totalcperr += cp_err

    if np.mean(pp_err) <= np.mean(np_err) and np.mean(pp_err) <= np.mean(spp_err) and np.mean(pp_err) <= np.mean(cp_err):
        errppwins += 1
    if np.mean(np_err) <= np.mean(pp_err) and np.mean(np_err) <= np.mean(spp_err) and np.mean(np_err) <= np.mean(cp_err):
        errnpwins += 1
    if np.mean(spp_err) <= np.mean(pp_err) and np.mean(spp_err) <= np.mean(np_err) and np.mean(spp_err) <= np.mean(cp_err):
        errsppwins += 1
    if np.mean(cp_err) <= np.mean(pp_err) and np.mean(cp_err) <= np.mean(np_err) and np.mean(cp_err) <= np.mean(spp_err):
        errcpwins += 1

    # By residuals
    np_res = np.absolute(b - np.dot(A, np_soln))
    pp_res = np.absolute(b - np.dot(A, pp_soln))
    spp_res = np.absolute(b - np.dot(A, spp_soln))
    cp_res = np.absolute(b - np.dot(A, cp_soln))
    totalnpres += np_res
    totalppres += pp_res
    totalsppres += spp_res
    totalcpres += cp_res

    if np.mean(pp_res) <= np.mean(np_res) and np.mean(pp_res) <= np.mean(spp_res) and np.mean(pp_res) <= np.mean(cp_res):
        resppwins += 1
    if np.mean(np_res) <= np.mean(pp_res) and np.mean(np_res) <= np.mean(spp_res) and np.mean(np_res) <= np.mean(cp_res):
        resnpwins += 1
    if np.mean(spp_res) <= np.mean(pp_res) and np.mean(spp_res) <= np.mean(np_res) and np.mean(spp_res) <= np.mean(cp_res):
        ressppwins += 1
    if np.mean(cp_res) <= np.mean(pp_res) and np.mean(cp_res) <= np.mean(np_res) and np.mean(cp_res) <= np.mean(spp_res):
        rescpwins += 1

    print("Run :", k)

print("\nTotal runs: ", runs)

print("\nStats by forward error:")
print("NP Wins: ", errnpwins)
print("PP Wins: ", errppwins)
print("SPP Wins: ", errsppwins)
print("CP Wins: ", errcpwins)
print("NP mean error element: ", np.mean(totalnperr)/runs)
print("PP mean error element: ", np.mean(totalpperr)/runs)
print("SPP mean error element: ", np.mean(totalspperr)/runs)
print("CP mean error element: ", np.mean(totalcperr)/runs)

print("\nStats by residuals:")
print("NP Wins: ", resnpwins)
print("PP Wins: ", resppwins)
print("SPP Wins: ", ressppwins)
print("CP Wins: ", rescpwins)
print("NP mean residual element: ", np.mean(totalnpres)/runs)
print("PP mean residual element: ", np.mean(totalppres)/runs)
print("SPP mean residual element: ", np.mean(totalsppres)/runs)
print("CP mean residual element: ", np.mean(totalcpres)/runs)

'''

The procedure is as follows. First, a matrix A and a vector x are constructed.
The b is computed as A*x. Next, I pretend that I don't know x, so I solve the
problem Ax = b for x with the constructed values for A and b. The direct error
is then calculated as |x - x'| where x' is the solution found for x by the
algorithms in this file. The residual error is calculated as |b - Ax'|.

All of this is done for a large number of trials. The mean direct error is the
mean of all the direct error vectors for one of the solution methods (partial
pivoting, scaled partial pivoting, etc.). The mean that is printed to the console
is the mean element in this mean vector.

'''
