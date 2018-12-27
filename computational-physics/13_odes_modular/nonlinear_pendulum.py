#! /usr/bin/env python
"""
The nonlinear pendulum equation has the form

    d^2(theta)/dt^2 = -(g/L)*sin(theta)

This can be converted to the pair of simultaneous first-order ODEs:

    d(omega)/dt = -(g/L)*sin(theta)
    d(theta)/dt = omega

nonlinear_pendulum.py solves this system of ODEs using the fourth-order Runge-Kutta
method.

Leon Hostetler, Apr. 9, 2017

USAGE: python nonlinear_pendulum.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import mymodule_ODEs as mmo
import numpy as np


def f(r, t):
    """
    Write the set of first-order ODEs
        d(omega)/dt = -(g/L)*sin(theta)
        d(theta)/dt = y
    as a single vectorized function of the form
        f(r,t) = dr/dt.
    """
    g = 9.81    # [m/s^2]
    L = 0.1     # [m]

    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/L)*np.sin(theta)

    return np.array([ftheta, fomega], float)


# Constants
tMin, tMax, N = 0.0, 5.0, 1000
h = (tMax - tMin)/N

# Create a Runge-Kutta object, and pass our function to it.
rk = mmo.RungeKutta(f)

# The list of points for time, x(t), and y(t)
tPoints = np.arange(tMin, tMax, h)
thetaPoints, omegaPoints = [], []

# Initialize the list of function values with the initial conditions
theta_0 = 179  # Starting angle in degrees
r = np.array([np.pi*theta_0/180, 0], float)

# Apply the Runge-Kutta method
for t in tPoints:
    thetaPoints += [r[0]]
    omegaPoints += [r[1]]
    r += rk(r, t, h)

# Display the results
plt.rc('text', usetex=True)

plt.figure(1)
plt.subplot(211)
title = "Nonlinear Pendulum with Starting Angle of " + str(theta_0) + r"$^{\circ}$"
plt.title(title)
plt.plot(tPoints, thetaPoints)
plt.xlabel(r"$t$")
plt.ylabel(r"$\theta(t)$")

plt.subplot(212)
plt.plot(thetaPoints, omegaPoints)
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\frac{d\theta}{dt}$")
plt.show()
