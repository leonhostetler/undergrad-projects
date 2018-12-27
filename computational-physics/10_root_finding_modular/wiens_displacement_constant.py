#! /usr/bin/env python
"""
Uses the bisection method to find the root of
a nonlinear equation that allows us to calculate the Wien displacement constant.
We then use that to estimate the temperature of the surface of the sun.

Leon Hostetler, Mar. 23, 2017

USAGE: python wiens_displacement_constant.py
"""

from __future__ import division, print_function
import mymodule_root_finding as mmr
import numpy as np

#
# Constants
#

h = 6.62606957e-34      # [J/s]
c = 2.99792458e8        # [m/s]
kB = 1.3806488e-23      # [m^2 kg / s^2 K]
lam = 5.02e-7           # [m], wavelength peak of sun's radiation

#
# Define the polynomial and compute the nonzero root.
#

def f(x):
    """
    The polynomial we want to find the roots of.
    """
    return 5*np.exp(-x) + x - 5

root = mmr.bisection(f, 1, 10, 1e-6)[0]
print("\nx = ", root, sep="")
b = (h*c)/(root*kB)
print("Wien displacement constant: b = ", b, sep="")

#
# Estimate the temperature of the sun. We know that lambda = b/T, where
# b = (hc)/(x kB), so T = b/lambda.
#

T = b/lam
print("\nOur estimation of the temperature of the sun's surface is ", int(T), "K.", sep="")
