#! /usr/bin/env python
"""
A simple program that uses the semi-empirical
mass formula to calculate the approximate nuclear binding energy
of an atomic nucleus given the atomic and mass numbers of an atom.

Leon Hostetler, Jan. 20, 2017

USAGE: python mass_formula.py

"""
from __future__ import division, print_function

# Main body of program

a1 = 15.67  # Constants are in millions of eV
a2 = 17.23
a3 = 0.75
a4 = 93.2

Z = int(raw_input("Enter the atomic number (Z): "))
A = int(raw_input("Enter the mass number (A): "))

a5 = 0  # Initialize
if Z % 2 == 0 and (A-Z) % 2 == 0:
    a5 = 12.0
elif Z % 2 != 0 and (A-Z) % 2 != 0:
    a5 = -12.0
else:
    a5 = 0

B = a1*A - a2*A**(2/3) - a3*(Z**2/A**(1/3)) - a4*((A - 2*Z)**2/A) + a5/A**(1/2)

print("The binding energy of the atom is ", B, " MeV.")
print("The binding energy per nucleon is ", B/A, " MeV.")
