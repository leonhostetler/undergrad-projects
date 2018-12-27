#! /usr/bin/env python
"""

Plot the first several terms of a Taylor series and compare with the plot
of the actual function being approximated by the Taylor series.

Leon Hostetler, Jan. 14, 2017

USAGE: python plot_partial_series.py

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

lower = 0       # Lower limit on sum
upper = 1       # Upper limit on sum
res = 1000      # Plotting resolution
left = -np.pi   # Graph bounds
right = np.pi

#
# Enter the summand here. Your variable is x and your summation index is k
#
def summand(x, k):
    return (1.0/np.math.factorial(2*k)-(3.0*x)/np.math.factorial(2*k+1))*(x**(2*k))*((-1)**k)


#
# Compute the graph points for the partial sum. No need to change
# anything below here.
#
X = np.linspace(left, right, res)  # Generate the x-values
def partial_sum(x, a, b):  # Function that gives the partial sum
    f = np.array([summand(x, k) for k in range(a, b+1)])
    return f.sum()

Y = np.array([partial_sum(i, lower, upper) for i in X])  # Compute the y-values

#
# Compute the graph points for the true function.
#
def fun(x):  # Define the true function here
    return np.cos(x) - 3*np.sin(x)

Y2 = np.array([fun(i) for i in X])  # Compute the y-values for the true function


#
# Plot both. The dashed plot gives the plot of the Taylor approximation
#
fig, ax = plt.subplots()
ax.plot(X, Y, linestyle='dashed')
ax.plot(X, Y2)
ax.grid()
axes = plt.gca()
plt.title(r'$P$' + '$_' + str(upper) + '$' + r'$(x)$')
axes.set_xlim([left, right])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()
