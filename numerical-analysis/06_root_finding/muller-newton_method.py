#! /usr/bin/env python
"""

Find all (including complex) roots of a given polynomial by using a combination
of Newton's method, Muller's method, and polynomial deflation.

Leon Hostetler, Feb. 26, 2017

USAGE: python muller-newton_method.py

"""
from __future__ import division, print_function
import numpy as np
import cmath


def newtons_method(x, a, tolerance):
    """
    This function returns a single root for a polynomial.
    Takes three parameters--a guess x of the root, the array
    of coefficients, and the error tolerance.
    """
    errormet = False
    notFoundFlag = False
    iterations = 0

    while errormet is False:

        fx = 0.0
        for i in range(len(a)):  # Calculate f(x)
            fx += a[i]*x**i

        fprimex = 0.0
        for i in range(1, len(a)):
            fprimex += i*a[i]*x**(i-1)

        x_new = x - fx/fprimex

        iterations += 1
        if abs(x_new - x) < tolerance:
            errormet = True
            print("Newton iterations = ", iterations)

        x = x_new

        # If you do 10,000 Newton iterations and still no root
        # then the remaining roots are probably complex. Stop.
        if iterations > 10000:
            return 0.0, True

    return x_new, notFoundFlag


def mullers_method(x0, x1, x2, coeff, tolerance):
    """
    Mullers method finds a single complex root of a function given three
    guess values.

    May not be able to handle multiplicities
    """
    errorMet, iterations = False, 0

    while errorMet is False:

        # Evaluate the polynomial at the three points
        fx0, fx1, fx2 = 0.0, 0.0, 0.0
        for i in range(len(coeff)):
            fx0 += coeff[i] * x0 ** i
        for i in range(len(coeff)):
            fx1 += coeff[i] * x1 ** i
        for i in range(len(coeff)):
            fx2 += coeff[i] * x2 ** i

        # Construct the interpolating quadratic
        a = ((fx2-fx1)/(x2-x1)-(fx1-fx0)/(x1-x0))/(x2-x0)
        b = (fx2-fx1)/(x2-x1)+(x2-x1)*a
        c = fx2

        # Find a root of the interpolating quadratic
        # Select the root that gives the largest (abs) denominator
        if b < 0:
            x3 = x2 - (2*c)/(b - cmath.sqrt(b*b - 4*a*c))
        else:
            x3 = x2 - (2*c)/(b + cmath.sqrt(b*b - 4*a*c))

        iterations += 1

        if abs(x3-x2) < tolerance:
            print("Muller iterations: ", iterations)
            errorMet = True

        x0, x1, x2 = x1, x2, x3

        if iterations > 10000:
            print("Something went wrong! 10,000 iterations were exceeded.")
            quit()

    return x3


def deflate_polynomial(a, r):
    """
    #Given a polynomial with coefficients in matrix a and a root r of
    #the polynomial, deflate the polynomial and return the result.
    """

    k = len(a) - 1
    b = np.zeros([k], dtype=complex)

    b[k-1] = a[k]
    for i in range(k-1, 0, -1):
        b[i-1] = a[i] + r*b[i]

    return b



# Enter the ordered coefficients of your polynomial here.
# Order them starting with the zero order term as in
#    f(x) = a_0 + a_1x^1 + a_2x^2 + ...
#coefficients = np.array([0.0, 15.0, 0.0, -70.0, 0.0, 63.0])
#coefficients = np.array([0.0, 13.125, 0.0, -78.75, 0.0, 86.625])  # P_6'(x)
#coefficients = np.array([1, 2, 3, 4, 5, 6])
#coefficients = np.array([4.0, 0.0, -3.0, 1.0])  # Has multiplicity
coefficients = np.array([1.0, 0.0, 0.0, 0.0, 1.0])  # Has complex roots
#coefficients = np.array([0.001, 1000, 0.001])  # Has complex roots

coefficients2 = np.copy(coefficients)

Tol = 1.0e-10

# Find the roots using Newton's Method
k = len(coefficients) - 1
print("\nNewton's Method:")
while k >= 1:
    rootAndFlag = newtons_method(1.0, coefficients, Tol)
    root = rootAndFlag[0]
    flag = rootAndFlag[1]

    if flag is True:
        print("The remaining roots were not found. They are probably complex.")
        break

    elif abs(root.real) < 1e-15:     # Assume root is zero
        root = 0.0

    print(root.real)
    B = deflate_polynomial(coefficients, root)
    coefficients = B
    k -= 1

# Find the roots using Muller's method
k = len(coefficients2) - 1
print("\nMullers's Method:")
while k >= 1:
    root = mullers_method(0.0, 1.0, 2.0, coefficients2, Tol)

    if (abs(root.real) < 1e-15) and (abs(root.imag) < 1e-15):
        root = 0.0
    elif abs(root.imag) < 1e-15:       # Assume imaginary part is zero
        root = root.real
    elif abs(root.real) < 1e-15:     # Assume real part is zero
        root = root.imag

    print(root)
    B = deflate_polynomial(coefficients2, root)
    coefficients2 = B
    k -= 1
