#! /usr/bin/env python
"""
Finds a single complex root of a given polynomial. Muller's
method is similar to Newton's method except, instead of finding the root of
a tangent line, we find the root of an interpolating quadratic.

Leon Hostetler, Mar. 3, 2017

USAGE: python mullers_method_single_root.py

"""
from __future__ import division, print_function
import cmath


def f(x):
    """
    The function we are trying to find a root of.
    """
    fx = x**4 + 1
    return fx


def mullers_method(x0, x1, x2, tolerance):
    """
    Mullers method finds a single complex root of a function given three
    guess values.
    """
    errorMet, iterations = False, 0

    while errorMet is False:

        # Construct the interpolating quadratic with the three points
        d = ((f(x2)-f(x1))/(x2-x1)-(f(x1)-f(x0))/(x1 - x0))/(x2 - x0)
        b = (f(x2)-f(x1))/(x2 - x1) + (x2 - x1)*d

        # Find a root of the interpolating quadratic
        disc = cmath.sqrt(b*b-4*d*f(x2))  # The discriminant

        # Select the root that gives the largest denominator
        if abs(b - disc) < abs(b + disc):
            x3 = x2 - (2*f(x2))/(b+disc)
        else:
            x3 = x2 - (2*f(x2))/(b-disc)

        # Is the error tolerance satisfied?
        if abs(x3-x2) < tolerance:
            errorMet = True

        x0, x1, x2 = x1, x2, x3

        if iterations > 10000:
            print("Something went wrong! 10,000 iterations were exceeded.")
            quit()

        iterations += 1

    return x3


Tol = 1.0e-10
root = mullers_method(-1, 0, 1, Tol)
print(root)



