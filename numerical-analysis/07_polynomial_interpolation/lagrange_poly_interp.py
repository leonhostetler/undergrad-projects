#! /usr/bin/env python
"""
Defines 5 different functions. After selecting a function,
the domain [-5, 5] is plotted along with P_n(x), the polynomial interpolant formed
using the Lagrange polynomial interpolating basis functions.

Leon Hostetler, Mar. 30, 2017

USAGE: python lagrange_poly_interp.py

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt


def fx(x, fcase):
    """
    Define the functions that you want to plot and interpolate.
    """
    if fcase == 0:
        f = 1.0/(1.0 + x*x)
    elif fcase == 1:
        f = np.sin(x)
    elif fcase == 2:
        if x < 0:
            f = -1.0
        else:
            f = 1.0
    elif fcase == 3:
        f = 2.0 - 0.4 * abs(x)
    elif fcase == 4:
        if x < 0:
            f = 1 + x*x/10
        else:
            f = 1 - x*x/10
    else:
        print("fcase invalid")

    return f


def lagrange_interp(xsten_list, fcase, n, x):
    """
    This method takes in a list of interpolating points xsten_list, a function
    fcase, the order n of the interpolating polynomial, and the value x at which
    you want f(x) to be approximated at. It returns y, the interpolated approximation
    of f(x).
    """

    # Construct the list of f(x) evaluated at x = the interpolating points
    fsten_list = [fx(xsten_list[i], fcase) for i in range(n+1)]

    y = 0.0
    for i in range(n+1):
        L = 1.0
        for j in range(n+1):
            if i != j:
                L = L * (x - xsten_list[j]) / (xsten_list[i] - xsten_list[j])
        y += fsten_list[i] * L

    return y


n = 10                  # The degree of the interpolating polynomial
fcase = 2               # Select the function to be plotted and interpolated
nplot = 1000            # Plotting resolution
xlo, xhi = -5.0, 5.0    # Define the plotting region
h = (xhi - xlo) / n     # Spacing between the interpolating points
xplot_list = []         # The list of x-values for f(x) and P_n(x)
fplot_list = []         # The list of y-values for P_n(x)
fexact_list = []        # The list of y-values for f(x)

# Create and fill the list of interpolating points
xsten_list = [xlo + k*h for k in range(n+1)]

for k in range(nplot+1):
    xplot = xlo + k*(xhi-xlo)/nplot
    fplot = lagrange_interp(xsten_list, fcase, n, xplot)
    xplot_list.append(xplot)
    fplot_list.append(fplot)
    fexact_list.append(fx(xplot, fcase))

# Plot the results
plt.plot(xplot_list, fplot_list, label='P_n(x)')
plt.plot(xplot_list, fexact_list, label='f(x)')
plt.legend(loc=1)
plt.xlabel("x")
plt.ylabel("P_n(x),f(x)")
plt.show()
