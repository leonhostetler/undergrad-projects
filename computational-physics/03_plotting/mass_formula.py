#! /usr/bin/env python
"""
Plot the binding energy per nucleon (for the most stable
isotope) for all the elements from Z = 1 to Z = 109.

Leon Hostetler, Feb. 2, 2017

USAGE: mass_formula.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt

# Main body of program

a1 = 15.67  # Constants are in millions of eV
a2 = 17.23
a3 = 0.75
a4 = 93.2

elements = []
bindingEnergies = []  # Binding energy per nucleon for most stable isotope

for Z in range(1, 110):         # For all elements from Z = 1 to Z = 109
    bindingEnergy = 0.0
    for A in range(Z, 3*Z+1):   # Find the nucleus with largest binding energy
        a5 = 0
        if Z % 2 == 0 and (A - Z) % 2 == 0:
            a5 = 12.0
        elif Z % 2 != 0 and (A - Z) % 2 != 0:
            a5 = -12.0
        else:
            a5 = 0
        # Here we use the semi-empirical mass formula
        B = a1*A - a2*(A**(2/3)) - a3*((Z**2)/(A**(1/3))) \
            - a4*(((A - 2*Z)**2)/A) + a5/(A**(1/2))

        if B/A >= bindingEnergy:
            bindingEnergy = B/A

    elements.append(Z)
    bindingEnergies.append(bindingEnergy)


plt.rc('text', usetex=True)
plt.plot(elements, bindingEnergies)
plt.title("Binding Energy per Nucleon")
plt.xlabel("Element (Z)")
plt.ylabel("Binding Energy (MeV)")
plt.savefig("plot.png")
plt.show()
