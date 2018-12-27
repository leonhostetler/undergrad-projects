#! /usr/bin/env python
"""
This file explores the use of ROOT's TLorentzVector class, which is useful
for working with energy-momentum 4-vectors.

Leon Hostetler, Apr. 16, 2017

USAGE: python lorentz_vectors.py
"""

from __future__ import division, print_function
from ROOT import TLorentzVector

# Create the energy-momentum vector for a photon with energy 5 GeV
photon = TLorentzVector(0, 0, 5.0, 5.0)

# Create the 4-vector for a proton at rest
proton = TLorentzVector(0, 0, 0, 0.938)

# Create vectors for two pi+ pions and one pi- pion
pip1, pip2, pim = TLorentzVector(), TLorentzVector(), TLorentzVector()

# Set the vector components for the pions
pip1.SetPxPyPzE(-0.226178, -0.198456, 1.946048, 1.974144)
pip2.SetPxPyPzE(0.554803, -0.301158, 1.301439, 1.453219)
pim.SetPxPyPzE(-0.07765, 0.072333, 1.372624, 1.38382)

# Print the magnitudes of each 4-vector
print("The magnitude of the photon 4-vector is", photon.Mag())
print("The magnitude of the proton 4-vector is", proton.Mag())
print("The magnitude of the pip1 4-vector is", pip1.Mag())
print("The magnitude of the pip2 4-vector is", pip2.Mag())
print("The magnitude of the pim 4-vector is", pim.Mag())

# Create a new 4-vector by adding/subtracting the others
diff = photon + proton - ( pip1 + pip2 + pim )

diffMass = diff.Mag()
print("The invariant mass of the missing particle is", diffMass)






