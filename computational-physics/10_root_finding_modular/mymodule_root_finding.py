#! /usr/bin/env python
"""
Module mymodule_root_finding.py is a module containing a collection of user-defined
functions for finding roots of polynomials and nonlinear equations.

Symbols and parameters:

    'f' is a user-defined function e.g. f(x) = x**2.
    'dfdx' is a user-defined function, the first derivative of f
    'x0' is a user-supplied guess
    'accuracy' is the level of precision you want
    'a' and 'b' are user-supplied guesses

Leon Hostetler, Mar. 21, 2017

USAGE: Used as a supplement to a main program.
"""

from __future__ import division, print_function
import numpy as np
import sys


def newton(f, dfdx, x0, accuracy=1e-10):
    """
    Newton's method for finding a root. Requires a function f, its
    derivative dfdx, a guess value x, and the required precision.
    """
    xlast = float("inf")

    i = 0
    while np.abs(x0 - xlast) > accuracy:
        xlast = x0
        x0 = xlast - f(xlast)/dfdx(xlast)
        i += 1

    return [x0, i]


def secant(f, a, b, accuracy=1e-10):
    """
    Secant method for finding a root. Requires a function f, two
    guess values a and b, and the required precision.
    """
    i = 0
    while np.abs(a - b) > accuracy:
        x = b - f(b)*(b-a)/(f(b) - f(a))
        a, b = b, x
        i += 1

    return [x, i]


def bisection(f, a, b, accuracy=1e-10):
    """
    This function defines the bisection (or binary search) method
    for finding the root of a function.
    """

    if f(a)*f(b) > 0:
        raise ValueError('Your bracketing values do not have opposite sign!')

    mid = 0.5 * (a + b)  # Midpoint

    if f(mid) == 0:
        return mid

    i = 0
    while np.abs(a - b) > accuracy:
        mid = 0.5 * (a + b)
        if f(mid)*f(a) > 0:
            a = mid
        else:
            b = mid
        i += 1

    return [mid, i]


def fposition(f, a, b, accuracy=1e-10):
    """
    This function defines the false position method
    for finding the root of a function.
    """

    if f(a)*f(b) > 0:
        raise ValueError('Your bracketing values do not have opposite sign!')

    x, xl = a, float("inf")

    i = 0
    while np.abs(x - xl) > accuracy:
        xl = x
        m = (f(b) - f(a))/(b - a)   # Compute the slope of the linear interpolant
        bInt = f(a) - m * a         # Compute y-intercept of linear interpolant
        x = -bInt / m
        if f(x) == 0:
            return [x, i]
        if f(x) * f(a) > 0:
            a = x
        else:
            b = x
        i += 1

    return [x, i]


def f(x):
    """
    Define a function used to test the root-finding methods
    """
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1


def dfdx(x):
    """
    The first derivative of the function defined above. This is
    required to test Newton's method.
    """
    return 5544*x**5 - 13860*x**4 + 12600*x**3 - 5040*x**2 + 840*x - 42


def test_functions():
    """
    This function tests the various numerical integration functions in this module.
    To execute test of function run module as python program along with commandline
    argument "test" example: "mypython test"
    """

    isGood = True

    # Test Newton's method
    root = newton(f, dfdx, 0, 1e-10)[0]
    if abs(root - 0.0337652429) > 1e-10:
        print("WARNING: newton() failed the test.")
        isGood = False

    # Test secant method
    root = secant(f, 0, 0.05, 1e-10)[0]
    if abs(root - 0.0337652429) > 1e-10:
        print("WARNING: secant() failed the test.")
        isGood = False

    # Test bisection method
    root = bisection(f, 0, .05, 1e-10)[0]
    if abs(root - 0.0337652429) > 1e-10:
        print("WARNING: bisection() failed the test.")
        isGood = False

    # Test false position method
    root = bisection(f, 0, .05, 1e-10)[0]
    if abs(root - 0.0337652429) > 1e-10:
        print("WARNING: fposition() failed the test.")
        isGood = False

    if isGood is True:
        print("Module is good.")

# TEST BLOCK
# The test block only executes if the module is run as a main program
# and if the word "test" is given on the command line.
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_functions()
