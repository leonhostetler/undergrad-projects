#! /usr/bin/env python
"""

Finds a single root of a given polynomial.

Leon Hostetler, Feb. 26, 2017

USAGE: python newtons_method_single_root.py

"""
from __future__ import division, print_function

def f(x):
    """
    Define the polynomial.
    """
    return 15*x - 70*x**3 + 63*x**5


def f_prime(x):
    """
    Define the derivative of the polynomial.
    """
    return 15 - 210*x**2 + 315*x**4


def newtons_method(x, tolerance):
    """
    This function returns a single root for the polynomial defined
    in f(x). Takes two parameters--a guess x and the error tolerance.
    """
    errormet = False

    while errormet is False:
        x_new = x - f(x)/f_prime(x)

        if abs(x_new - x) < tolerance:
            errormet = True

        x = x_new

    return x_new


root = newtons_method(1.0, 1.0e-10)
print(root)
