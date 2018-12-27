#! /usr/bin/env python
"""
Compute the transmission and reflection probabilities of a
particle with a given mass and energy encountering a potential step.

Leon Hostetler, Feb. 14, 2017

USAGE: python quantum_step.py
"""

from __future__ import division, print_function

# Constants
m = 9.11e-31        # Mass of particle (kg)
eV = 1.6022e-19     # Convert eV to Joules
E = 10.0*eV         # Energy of incoming particle (J)
V = 9.0*eV          # Height of potential step (J)
h = 1.0546e-34      # h-bar (m^2 kg / s)

# Calculations
k1 = (2*m*E)**(1/2)/h
k2 = ((2*m*(E-V))**(1/2))/h
T = (4*k1*k2)/(k1+k2)**2    # Transmission probability
R = ((k1-k2)/(k1+k2))**2    # Reflection probability

# Print results
print("The transmission probability is ", "{0:.2f}".format(T), ".", sep="")
print("The reflection probability is ", "{0:.2f}".format(R), ".", sep="")
print("As a check, the total probability is the sum of the two: ", "{0:.2f}".format(T+R), ".", sep="")
