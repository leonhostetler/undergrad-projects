#! /usr/bin/env python
"""
Displays an animation of a pendulum undergoing simple harmonic motion.

Leon Hostetler, Feb. 14, 2017

USAGE: python fancy_simple_pendulum.py
"""

from __future__ import division, print_function
from visual import *
import numpy as np
#from PIL import ImageGrab


#scene = display(title='Fancy Simple Pendulum',
#                x=0, y=0, width=700, height=700,
#                center=(0, -3, 0),
#                forward=(-1, 0, -1))  # Camera direction


# Set the constants
g = 9.80            # (m/s^2)
L = 10              # Length of the pendulum
initialAngle = 1.3  # In radians


# Make the pendulum bob, a small ceiling, a hinge, and the rod.
position = [L*np.sin(initialAngle), -L*np.cos(initialAngle), -0.15]
pend = cylinder(pos=position, axis=(0, 0, 0.3), radius=1)
box(pos=(0, 0.25, -2.6), length=10, height=0.5, width=5)
box(pos=(0, 0.25, 2.6), length=10, height=0.5, width=5)
cylinder(pos=(0, 0, -0.15), axis=(0, 0, 0.3), radius=0.4)
rod = cylinder(pos=(0, 0, 0), axis=(pend.pos[0], pend.pos[1], 0), radius=0.1)


def position(time):
    """
    Given time, t, this function moves the pendulum to its new position. We
    use the equation:
        theta(t) = theta_0*cos(sqrt(g/L)*t)
    """
    theta = initialAngle*np.cos((g/L)**(1/2)*time)          # Angle of the pendulum
    pend.pos = [L*np.sin(theta), -L * np.cos(theta), -0.15] # Update position of bob
    rod.axis = [pend.pos[0], pend.pos[1], 0]                # Update rod's position


i = 0
while True:
    rate(100)
    if scene.mouse.clicked:
        m = scene.mouse.getclick()
        angle = np.arctan2(m.pos[0], -m.pos[1])
        pend.pos = [L * np.sin(angle), -L * np.cos(angle), -0.15]
        rod.axis = [pend.pos[0], pend.pos[1], 0]
        initialAngle = angle
    else:
        position(i)
        i += 0.01
#        if (int(i*100)) % 5 == 0:
#            im = ImageGrab.grab((10, 30, 690, 690))
#            im.save('Images/filename' + str(int(i*100)) + '.jpg')
