#! /usr/bin/env python
"""
A simple program that gives orbit characteristics for
elliptical planetary orbits, given the distance to the sun and the velocity
at perihelion.

Leon Hostetler, Jan. 22, 2017

USAGE: python planetary_orbits.py

"""
from __future__ import division, print_function
import numpy as np

# Main body of program

G = 6.6738e-11  # Universal gravitational constant
M = 1.9891e30   # Mass of Earth


l1 = float(raw_input("Enter the distance to the sun at perihelion (m): "))
v1 = float(raw_input("Enter the linear speed at perihelion (m/s): "))


v2 = (2*G*M)/(l1*v1) - v1   # Linear speed at aphelion
l2 = (l1*v1)/v2             # Distance from sun at aphelion
a = (l1 + l2)/2             # Semi-major axis
b = (l1*l2)**(1/2)          # Semi-minor axis
T = (2*np.pi*a*b)/(l1*v1)   # Orbital period
e = (l2 - l1)/(l2 + l1)     # Orbital eccentricity

print("The distance at aphelion is ", l2, " meters.")
print("The linear speed at aphelion is ", v2, " meters per second.")
print("The orbital period is ", T, " seconds, or ", T/31536000, " years.")
print("The orbital eccentricity is ", e, ".")
