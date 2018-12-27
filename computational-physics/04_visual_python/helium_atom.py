#! /usr/bin/env python
"""
Display an animation of the classical helium atom with
four nucleons and a pair of electrons orbiting orthogonally.

Leon Hostetler, Feb. 9, 2017

USAGE: helium_atom.py
"""
from __future__ import division, print_function
import numpy as np
from visual import sphere, color, rate

nucleonSize = 0.1
electronSize = 0.05

# Constructing the lithium nucleus
sphere(pos=[0.1, 0.0, 0.0], radius=nucleonSize, color=color.blue)
sphere(pos=[-0.1, 0.0, 0.0], radius=nucleonSize, color=color.blue)
sphere(pos=[0.0, 0.1, 0.0], radius=nucleonSize, color=color.red)
sphere(pos=[0.0, -0.1, 0.0], radius=nucleonSize, color=color.red)

# Add the electrons
electron1 = sphere(pos=[1, 0, 0], radius=electronSize, make_trail=True)
electron2 = sphere(pos=[0, 1, 0], radius=electronSize, make_trail=True)

# Animate the system
radius = 2
while True:
    for theta in np.arange(0, 50*np.pi, 0.1):
        rate(75)
        x = np.cos(theta)
        y = np.sin(theta)
        electron1.pos = [x, y, 0]
        electron2.pos = [0, x, y]
