#! /usr/bin/env python
"""
A simple program computes the height of a satellite above Earth given its period.

Leon Hostetler, Jan. 22, 2017

USAGE: python satellite_altitude.py

"""
from __future__ import division, print_function
import numpy as np

# Main body of program

G = 6.67e-11    # Universal gravitational constant
M = 5.97e24     # Mass of Earth
R = 6.3713e6    # Radius of Earth

T = int(raw_input("Enter the period of the satellite (seconds): "))

# Compute the height of the satellite
h = ((G*M*T**2)/(4*np.pi**2))**(1/3) - R

print("The altitude of the satellite is ", h, " meters.")
