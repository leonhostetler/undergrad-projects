#! /usr/bin/env python
"""
Finds all the roots of a given polynomial. The first root
is found using Newton's method, then the polynomial is deflated and the
process is repeated until all the roots are found.

Leon Hostetler, Feb. 26, 2017

USAGE: python newtons_method_all_roots.py

"""
from __future__ import division, print_function
import numpy as np


def newtons_method(x, a, tolerance):
    """
    This function returns a single root for a polynomial.
    Takes three parameters--a guess x of the root, the array
    of coefficients, and the error tolerance.
    """
    errormet = False
    notFoundFlag = False
    iterations = 0.0

    while errormet is False:

        fx = 0.0
        for i in range(len(a)):  # Calculate f(x)
            fx += a[i]*x**i

        fprimex = 0.0
        for i in range(1, len(a)):
            fprimex += i*a[i]*x**(i-1)

        x_new = x - fx/fprimex

        if abs(x_new - x) < tolerance:
            errormet = True

        x = x_new
        iterations += 1

        # If you do 10,000 Newton iterations and still no root
        # then the remaining roots are probably complex. Stop.
        if iterations > 10000:
            return 0.0, True

    return x_new, notFoundFlag


def deflate_polynomial(a, r):
    """
    Given a polynomial with coefficients in matrix a and a root r of
    the polynomial, deflate the polynomial and return the result.
    """

    k = len(a) - 1
    b = np.zeros([k])

    b[k-1] = a[k]
    for i in range(k-1, 0, -1):
        b[i-1] = a[i] + r*b[i]

    return b


# Enter the ordered coefficients of your polynomial here.
# Order them starting with the zero order term as in
#    f(x) = a_0 + a_1x^1 + a_2x^2 + ...
#coefficients = np.array([0.0, 15.0, 0.0, -70.0, 0.0, 63.0])
coefficients = np.array([0.0, 13.125, 0.0, -78.75, 0.0, 86.625])  # P_6'(x)
#coefficients = np.array([4.0, 0.0, -3.0, 1.0])  # Has multiplicity
#coefficients = np.array([1.0, 0.0, 0.0, 1.0])  # Has complex roots
#coefficients = np.array([0.001, 1000, 0.001])  # Has complex roots

k = len(coefficients) - 1
Tol = 1.0e-10

while k >= 1:
    rootAndFlag = newtons_method(1.0, coefficients, Tol)
    root = rootAndFlag[0]
    flag = rootAndFlag[1]

    if flag is True:
        print("The remaining roots were not found. They are probably complex.")
        break

    print(root)
    B = deflate_polynomial(coefficients, root)
    coefficients = B
    k -= 1
