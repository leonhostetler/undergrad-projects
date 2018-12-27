#! /usr/bin/env python
"""
Finds the equilibrium angle for a mass on two springs. This
involves find the root of a nonlinear equation. This root is found using four
different methods--the bisection method, the false position method, Newton's
method, and the secant method.

Leon Hostetler, Mar. 25, 2017

USAGE: python mass_springs.py
"""

from __future__ import division, print_function
import mymodule_root_finding as mmr
import numpy as np

#
# Constants
#

g = 9.8         # [m / s^2]
k = 1000.0      # [N/m]
m = 5.0         # [kg]
L = 0.3         # [m]

#
# Define the function and its derivative
#


def f(x):
    """
    The function we want to find the root of
    """
    return np.tan(x) - np.sin(x) - (m*g)/(2*k*L)


def dfdx(x):
    """
    The first derivative of the polynomial.
    """
    return (1/np.cos(x))**2 - np.cos(x)


#
# Find the root using the four different methods.
#
bisection = mmr.bisection(f, 0, np.pi/2, 1e-14)
print("\nBisection method:")
print("theta = ", bisection[0], ", iterations = ", bisection[1], sep="")

fposition = mmr.fposition(f, 0.1, 1, 1e-14)
print("\nFalse position method:")
print("theta = ", fposition[0], ", iterations = ", fposition[1], sep="")

newton = mmr.newton(f, dfdx, np.pi/4, 1e-14)
print("\nNewton's method:")
print("theta = ", newton[0], ", iterations = ", newton[1], sep="")

secant = mmr.secant(f, 0.1, 1, 1e-14)
print("\nSecant method:")
print("theta = ", secant[0], ", iterations = ", secant[1], sep="")
