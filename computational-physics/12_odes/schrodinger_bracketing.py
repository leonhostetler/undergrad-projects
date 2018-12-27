#! /usr/bin/env python
"""
Solves Schrodinger's time independent equation for
two energy values which bracket the lowest energy eigenvalue.

Leon Hostetler, Apr. 25, 2017

python shrodinger_bracketing.py
"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


def V(x):
    """The symmetric potential function."""
    return x**2


def f(r, x, E):
    """
    Write the set of first-order ODEs
        d(phi)/dx = 2[V(x) - E]psi
        d(psi)/dx = phi
    as a single vectorized function of the form
        f(r,x) = dr/dx.
    """

    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = 2*(V(x) - E)*psi

    return np.array([fpsi, fphi], float)


def rk4(func, r, t, h, E):
    """
    4th order Runge-Kutta method for solving 1st order differential equations

    func:  user defined function for the 1st order differential equations
    r: dependent variable
    x: independent variable
    h: independent variable step size
    """
    k1 = h*func(r, t, E)
    k2 = h*func(r + 0.5*k1, t + 0.5*h, E)
    k3 = h*func(r + 0.5*k2, t + 0.5*h, E)
    k4 = h*func(r+k3, t+h, E)
    return (k1 + 2*k2 + 2*k3 + k4)/6


def waveFunction(f, r, xValues, deltaX, E):
    """
    Solve for the wave function using the 4th order Runge Kuttta method
    to solve for the values for the wavefunction for a given value of the
    energy E.

    Note: The wave function is not necessarily an eigenfunction. It is only
    an eigenfunction if E happens to be an eigenvalue.
    an eigenvalue.
    """
    # make a copy of the initial values so that this function can be
    # repeatedly called with the same initial values
    s = np.copy(r)

    psi = []
    for x in xValues:
        psi += [s[0]]
        s += rk4(f, s, x, h, E)

    return np.array(psi, float)


def plot_wavefunction(x, psi, parity, E):
    """
    Plot the wavefunction of a given parity. Use symmetry to
    extend the wavefunction to the left of x = 0.
    """
    if parity % 2 == 0:
        psi = np.append(psi[::-1], psi[1:])
    else:
        psi = np.append(-psi[::-1], psi[1:])

    x = np.append(-x[::-1], x[1:])

    label = r"$\psi(x), \,E = " + str(E) + "$"

    plt.plot(x, psi, label=label)


#######################################################################
#                               MAIN
#######################################################################

# Assume a symmetric V(x)
xMin, xMax, N = 0.0, 4.0, 1000
h = (xMax - xMin)/N

# The list of points for time, x(t), and y(t)
xValues = np.arange(xMin, xMax, h)

# Initialize the plot
plt.rc('text', usetex=True)
plt.title("Numerical Solutions of 1D Schrodinger Equation")

# The 'parity' variable keeps track of the parity of the eigenstates.
parity = 0
if parity % 2 == 0:
    r = np.array([1.0, 0.0], float)
else:
    r = np.array([0.0, 1.0], float)

# Find a bracketing interval of the lowest energy eigenvalue
E, dE, bracket = 0.0, 0.1, False
while bracket is False:
    psi1 = waveFunction(f, r, xValues, h, E)
    E += dE
    psi2 = waveFunction(f, r, xValues, h, E)
    if (psi1[len(psi1)-1] < 0) != (psi2[len(psi1)-1] < 0):
        bracket = True
        plot_wavefunction(xValues, psi1, parity, E-dE)
        plot_wavefunction(xValues, psi2, parity, E)

    if E > 1000:
        print("Bracketing interval not found!")
        break

xValues = np.append(-xValues[::-1], xValues[1:])

# Plot the potential V(x) as well
vValues = [V(i) for i in xValues]

plt.plot(xValues, vValues, label=r"$V(x)$", linestyle='dashed')
plt.legend(loc=1)
plt.xlabel(r"$x$")
plt.grid(True)
plt.ylim((-2, 2))
plt.show()
