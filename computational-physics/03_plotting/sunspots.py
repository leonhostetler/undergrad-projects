#! /usr/bin/env python
"""
Plot the observed number of sunspots for each month.

Leon Hostetler, Feb. 2, 2017

USAGE: sunspots.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

# Main body of program

r = 5  # The 'half-length' of the weighted average

# Load the data from the file
data = np.loadtxt("sunspots.txt", float)
x = data[0:1001, 0]
y = data[0:1001, 1]

# Compute the weighted average
X = x[r:len(x)-r]
Y = []
for k in range(r, len(x)-r):
    avg = 0
    for m in range(k-r, k+r+1):
        avg += y[m]
    Y.append(avg/(2*r+1))

# Plot the results
plt.plot(x, y, linewidth=.5, c="g")
plt.plot(X, Y, linewidth=2, c="k")
plt.title("Sunspots per Month")
plt.xlabel("Month")
plt.ylabel("Number of Sunspots")
plt.savefig("sunpots.png")
plt.show()
