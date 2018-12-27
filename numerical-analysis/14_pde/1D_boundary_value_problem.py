#! /usr/bin/env python
"""

Numerically solves the Sturm-Liouville equation

        -( p y' )' + qy = f

where p, q, and f are all functions of x, on the interval 0 < x < 1 with the
boundary conditions

        y(0) = y_0
        y'(1) = 0

Leon Hostetler, Apr. 26, 2017

USAGE: python 1D_boundary_value_problem.py

"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


def p(x):
    if x > 0.5:
        return 1.0
    else:
        return 0.001
    #return 1


def q(x):
    return 0.0


def f(x):

    if x < .9:
        return 0.0
    else:
        return 10.0

    #return np.exp(-x**2)


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


##################################################################
#                              MAIN
##################################################################

# Set the number of intervals
n = 100     # Number of intervals
h = 1/n     # Interval width
y0 = 1      # Left boundary condition

TOLfactor = 1e-7  # Error tolerance for BICGSTAB method

# Define the domain
x = np.linspace(0, 1, n+1)

# Define the b-vector
b = [0.5*h*f((x[0]+x[1])/2) + 0.5*h*f((x[1]+x[2])/2) + \
     (y0/h)*p((x[0]+x[1])/2) - (y0*h/6)*q((x[0]+x[1])/2)]  # The b-vector containing the first element

for i in range(2, n):
    b += [0.5*h*f((x[i-1]+x[i])/2) + 0.5*h*f((x[i]+x[i+1])/2)]

b += [0.5*h*f((x[n-1]+x[n])/2)]  # Add last element in b

# Define the diagonal elements of A
D = []
for i in range(1, n):
    a1 = (1/h)*p((x[i-1]+x[i])/2)
    a2 = (1/h)*p((x[i]+x[i+1])/2)
    a3 = (h/3)*q((x[i-1]+x[i])/2)
    a4 = (h/3)*q((x[i]+x[i+1])/2)
    D += [a1 + a2 + a3 + a4]

D += [(1/h)*p((x[n-1]+x[n])/2) + (h/3)*q((x[n-1]+x[n])/2)]  # Last diagonal element

# Define the off-diagonal elements of A
U, L = [], []
for i in range(1, n):
    a1 = (-1/h)*p((x[i]+x[i+1])/2) + (h/6)*q((x[i]+x[i+1])/2)
    U += [a1]
    L += [a1]


# Compute the coefficients using the BICGSTAB algorithm for a sparse matrix system
y = BICGSTAB(n, D, U, L, b)[0]
y = np.hstack(([y0], y))  # Insert y0 as first element


#
# NOTE: Be mindful of the plotting scale. Python automatically scales the plots
# so that an effectively horizontal line looks nothing like a horizontal line.
#
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
