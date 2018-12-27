#! /usr/bin/env python
"""
Finds the root of a fifth degree polynomial to find the
distance from the center of Earth to the L1 Lagrange point between the
Earth and its moon.

Leon Hostetler, Mar. 25, 2017

USAGE: python lagrange_point.py
"""

from __future__ import division, print_function
import mymodule_root_finding as mmr

#
# Constants
#

G = 6.674e-11       # [m^3 / kg s^2]
M = 5.974e24        # [kg]
m = 7.348e22        # [kg]
R = 3.844e8         # [m]
w = 2.662e-6        # [1/s], omega

#
# Define the polynomial and its derivative
#


def f(r):
    """
    The polynomial we want to find the roots of.
    """
    return (w**2)*(r**5) - 2*R*(w**2)*(r**4) + (w*R)**2*(r**3) + (m-M)*G*(r**2) + 2*G*M*R*r - G*M*(R**2)


def dfdr(r):
    """
    The first derivative of the polynomial.
    """
    return 5*(w**2)*(r**4) - 8*R*(w**2)*(r**3) + 3*(w*R*r)**2 + 2*(m-M)*G*r + 2*G*M*R


#
# Find the root using Newton's method. We know the solution is between 0
# and R, so a reasonable starting guess is r = R/2.
#

root = mmr.newton(f, dfdr, R/2, 1e-6)[0]
print("\nr = ", root, sep="")
print("So the L1 Lagrange point is about ", int(root/1000), "km from the center of Earth.", sep="")
