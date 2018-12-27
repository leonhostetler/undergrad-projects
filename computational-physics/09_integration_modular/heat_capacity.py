#! /usr/bin/env python
"""
Create a graph of the heat capacity of aluminum as a function
of temperature. For each value of the temperature, the heat capacity is computed
using numerical integration.

Leon Hostetler, Mar. 7, 2017

USAGE: python heat_capacity.py
"""

from __future__ import division, print_function
import mymodule_integration as mmi
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """
    Define the integrand
    """
    return (x**4)*np.exp(x)/(np.exp(x) - 1)**2

def cv(T):
    """
    This function returns the heat capacity of a solid at temperature T.

    The constants below are for a sample of aluminum
    """
    V = 0.001       # [V] = m^3
    rho = 6.022e28  # [rho] = 1/m^3
    k = 1.3806e-23  # [k] = m^2 kg/(s^2 K), Boltzmann's constant
    theta = 428.0   # [theta] = K, the Debye temperatue

    epsilon = 1e-15  # Can't divide by zero

    integral = mmi.integrate_simpson(f, 0+epsilon, theta/T, 50)[0]
    CT = 9.0*V*rho*k*((T/theta)**3)*integral

    return CT


x = np.linspace(5, 500, 100)
y = cv(x)

# Plot the results
plt.rc('text', usetex=True)
plt.plot(x, y)
plt.legend([r"$C_V = 9 V \rho k_B \left( \frac{T}{\theta_D} \right)^3"
            r"\int_0^{\frac{\theta_D}{T}}\frac{x^4e^x}{(e^x-1)^2} dx$"])
plt.title("Heat Capacity of Aluminum")
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity")
plt.show()
