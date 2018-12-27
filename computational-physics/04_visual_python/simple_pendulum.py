#! /usr/bin/env python
"""
simple_pendulum.py displays an animation of a pendulum undergoing simple
harmonic motion.

Leon Hostetler, Feb. 14, 2017

USAGE: python simple_pendulum.py
"""

from __future__ import division, print_function
from visual import *
import numpy as np

#
# Constants
#

g = 9.80            # (m/s^2)
L = 10              # Length of the pendulum
initialAngle = 1.3  # In radians


#
# Create the pendulum bob and rod
#
pend = sphere(pos=(L*np.sin(initialAngle), -L*np.cos(initialAngle), 0), radius=1, color=color.yellow)
rod = cylinder(pos=(0, 0, 0), axis=(pend.pos[0], pend.pos[1], 0), radius=0.1)


def position(time):
    """
    Given time, t, this function moves the pendulum to its new position. We
    use the equation:
        theta(t) = theta_0*cos(sqrt(g/L)*t)
    """
    theta = initialAngle*np.cos((g/L)**(1/2)*time)          # Angle of the pendulum
    pend.pos = [L*np.sin(theta), -L * np.cos(theta), 0]     # Update position of bob
    rod.axis = [pend.pos[0], pend.pos[1], 0]                # Update rod's position


# Increment time
i = 0
while True:
    rate(100)
    position(i)
    i += 0.01
