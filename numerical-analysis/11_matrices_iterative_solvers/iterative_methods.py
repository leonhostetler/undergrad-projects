#! /usr/bin/env python
"""
This program uses the Jacobi, steepest descent, conjugate gradient, and BICGSTAB
methods to solve a sparse matrix of a specific kind.

Leon Hostetler, Feb. 5, 2017

USAGE: python iterative_methods.py

"""
from __future__ import division, print_function
import numpy as np


n = 2  # The size of the matrix
epsilon = .1
alpha = 1.0
beta = 10.0
TOLfactor = 1e-7  # Reduce residual by this factor

# Initialize the vectors
rho = np.zeros(n+1)
D = np.zeros(n)
U = np.zeros(n-1)
L = np.zeros(n-1)
B = np.zeros(n)


def generate_vectors(n, epsilon, alpha, beta):
    """
    This function generates the D, L, and U vectors corresponding to the
    specific sparse matrix, we are using in this program.
    """
    h = 1.0/n
    for i in range(n+1):
        ri = (i+1)*h
        if i == 0:
            rho[i] = epsilon
        elif i > 0 and ri <= 0.5:
            rho[i] = alpha
        elif ri > 0.5 and i < n:
            rho[i] = beta
        elif i == n:
            rho[i] = epsilon
    for i in range(n):
        ri = (i+1)*h
        B[i] = (h**2)*((1-ri)**2)*(ri**2)
        D[i] = rho[i] + rho[i+1]
    for i in range(n-1):
        U[i] = -rho[i+1]
        #L[i] = -rho[i+1]
        L[i] = U[i]


def print_matrices():
    """
    This function prints the matrix A for visualization purposes, as well as
    all of the vectors used in this program.
    """
    A = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            if j == i:
                A[i, j] = D[i]
            elif j == i-1:
                A[i, j] = L[i-1]
            elif j == i+1:
                A[i, j] = U[i]
            else:
                A[i, j] = 0
    print("A = ")
    print(A)
    print("B = ", B)
    print("D = ", D)
    print("U = ", U)
    print("L = ", L)
    print("rho = ", rho)


def Adotx(size, x, diagonal, upper, lower):
    """
    Computes the matrix-vector product Ax, where A is given as three
    diagonal band vectors.
    """
    z = np.zeros(size)
    z[0] = diagonal[0]*x[0] + upper[0]*x[1]
    for i in range(1, n-1):
        z[i] = diagonal[i]*x[i] + upper[i]*x[i+1] + lower[i-1]*x[i-1]
    z[n-1] = diagonal[n-1]*x[n-1] + lower[n-2]*x[n-2]
    return z


def residual(size, x, diagonal, upper, lower, b):
    """
    Computes the matrix-vector product Ax, where A is given as three
    diagonal band vectors.
    """
    res = np.abs(b - Adotx(size, x, diagonal, upper, lower))
    return res


def jacobi(size, diagonal, upper, lower, b):
    """
    For a tridiagonal matrix, this function takes in the size (i.e. number
    of rows in the square matrix), the vector b, and the three vectors
    corresponding to the diagonal, upper diagonal row, and lower diagonal row
    of the matrix. It returns the approximation x, as well as the number of
    Jacobi iterations that were performed.
    """
    k = 0
    x = np.zeros(n)
    TOL = TOLfactor*np.mean(residual(n, x, D, U, L, b))
    while np.mean(residual(n, x, D, U, L, b)) > TOL:
        X = np.zeros(n)
        X[0] = (b[0] - upper[0] * x[1]) / diagonal[0]
        for i in range(1, n-1):
            X[i] = (b[i] - lower[i-1]*x[i-1] - upper[i]*x[i+1])/diagonal[i]
        X[size-1] = (b[size-1] - lower[size-2]*x[size-2])/diagonal[size-1]
        x = X
        k += 1
        if k%1000 == 0:
            print("Jacobi k = ", k)
            print("Res = ", np.mean(residual(n, x, D, U, L, b)))
    return x, k


def steepest_descent(size, diagonal, upper, lower, b):
    """
    For a tridiagonal matrix, this function takes in the size (i.e. number
    of rows in the square matrix), the vector b, and the three vectors
    corresponding to the diagonal, upper diagonal row, and lower diagonal row
    of the matrix. It returns the approximation x, as well as the number of
    steepest descent iterations that were performed.
    """
    k = 0
    x = np.zeros(size)
    v = b - Adotx(size, x, diagonal, upper, lower)
    TOL = TOLfactor * np.mean(residual(n, x, D, U, L, b))
    while np.mean(np.absolute(v)) > TOL:
        t = (np.dot(v, v))/(np.dot(v, Adotx(size, v, diagonal, upper, lower)))
        x += t*v
        v = b - Adotx(size, x, diagonal, upper, lower)
        k += 1
        if k%1000 == 0:
            print("Steepest Descent k = ", k)
            print("Res = ", np.mean(residual(n, x, D, U, L, b)))
    return x, k


def conjugate_gradient(size, diagonal, upper, lower, b):
    """
    For a tridiagonal matrix, this function takes in the size (i.e. number
    of rows in the square matrix), the vector b, and the three vectors
    corresponding to the diagonal, upper diagonal row, and lower diagonal row
    of the matrix. It returns the approximation x, as well as the number of
    conjugate gradient iterations that were performed.
    """
    k = 0
    x = np.zeros(size)
    r1 = b - Adotx(size, x, diagonal, upper, lower)
    v = r1
    TOL = TOLfactor * np.mean(residual(n, x, D, U, L, b))
    while np.mean(np.absolute(v)) > TOL:
        t = np.dot(r1, r1)/np.dot(v, Adotx(size, v, diagonal, upper, lower))
        x += t*v
        r2 = r1 - t*Adotx(size, v, diagonal, upper, lower)
        s = np.dot(r2, r2)/np.dot(r1, r1)
        v = r2 + s*v
        r1 = r2
        k += 1
    return x, k


def BICGSTAB(size, diagonal, upper, lower, b):
    """
    For a tridiagonal matrix, this function takes in the size (i.e. number
    of rows in the square matrix), the vector b, and the three vectors
    corresponding to the diagonal, upper diagonal row, and lower diagonal row
    of the matrix. It returns the approximation x, as well as the number of
    BICGSTAB iterations that were performed.
    """
    k = 0
    x = np.zeros(size)
    r = b - Adotx(size, x, diagonal, upper, lower)
    rhat = r.copy()
    rho0, alpha, omega = 1, 1, 1
    v, p = np.zeros(size), np.zeros(size)
    TOL = TOLfactor * np.mean(residual(n, x, D, U, L, b))
    while np.mean(residual(n, x, D, U, L, b)) > TOL:
        k += 1
        rho1 = np.dot(rhat, r)
        beta = (rho1/rho0)*(alpha/omega)
        p = r + beta*(p - omega*v)
        v = Adotx(size, p, diagonal, upper, lower)
        alpha = rho1/np.dot(rhat, v)
        h = x + alpha*p
        if np.mean(residual(n, h, D, U, L, b)) < TOL:
            return h, k
        s = r - alpha*v
        t = Adotx(size, s, diagonal, upper, lower)
        omega = np.dot(t, s)/np.dot(t, t)
        x = h + omega*s
        if np.mean(residual(n, x, D, U, L, b)) < TOL:
            return x, k
        r = s - omega*t
        rho0 = rho1
    return x, k


generate_vectors(n, epsilon, alpha, beta)
print_matrices()

jSolution, jruns = jacobi(n, D, U, L, B)
sdSolution, sdruns = steepest_descent(n, D, U, L, B)
cgSolution, cgruns = conjugate_gradient(n, D, U, L, B)
BICGSTABSolution, BICGSTABruns = BICGSTAB(n, D, U, L, B)
print("\nJacobi iterations = ", jruns)
print("x = ", jSolution)
print("\nSteepest Descent iterations = ", sdruns)
print("x = ", sdSolution)
print("\nConjugate Gradient iterations = ", cgruns)
print("x = ", cgSolution)
print("\nBICGSTAB iterations = ", BICGSTABruns)
print("x = ", BICGSTABSolution)
