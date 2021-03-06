#! /usr/bin/env python
"""
Shows an animation of a two-pendulum newton's cradle. This
program shows only the spheres--think of the pendulum rods as being invisible.

Leon Hostetler, Feb. 16, 2017

USAGE: python newtons_cradle.py
"""
from __future__ import division, print_function
from visual import *
import numpy as np

# Constants
g = 9.80            # (m/s^2)
L = 10              # Length of the pendulums (m)
initialAngle = 0.5  # In radians

# Create the pendulum bob and rod
pend = sphere(pos=(L*np.sin(initialAngle), -L*np.cos(initialAngle), 0), color=color.yellow)
pend2 = sphere(pos=(-2, -L, 0), color=color.red)


def position(right, t):
    """
    Only one of the pendulums is in motion at a given time. This function
    moves the moving pendulum to its new position. We use the equation:
        theta(t) = theta_0*cos(sqrt(g/L)*t)
    """
    theta = initialAngle*np.cos((g/L)**(1/2)*t)

    if right:
        pend.pos = [L * np.sin(theta), -L * np.cos(theta), 0]  # Update position of bob
    else:
        pend2.pos = [L * np.sin(theta) - 2, -L * np.cos(theta), 0]

    # Once the moving pendulum reaches theta = 0, switch to the other one
    if theta <= 0:
        return False  # Return
    else:
        return True

# Increment time
i = 0
right = True  # The right pendulum is the first in motion
while True:
    rate(100)
    right = position(right, i)
    i += 0.01
