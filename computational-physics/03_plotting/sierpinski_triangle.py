#! /usr/bin/env python
"""
Plot the fractal triangle using a random method.

Leon Hostetler, Feb. 3, 2017

USAGE: sierpinski_triangle.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import random

# Main body of program

points = 10000  # The number of points to use.

x = []  # A list of x-coordinates
y = []  # A list of y-coordinates

# Set the starting point
point = [0, 0]
x.append(point[0])
y.append(point[1])

# Vertices of the triangle
vertices = [[-1.0, 0.0], [0.0, np.sqrt(3)], [1.0, 0.0]]


def new_point(p):
    """
    This function takes in a point p, chooses a random vertex
    of the triangle, then returns the midpoint between p and
    the random vertex.
    """
    v = random.choice(vertices)     # Choose a random vertex
    mid = [0, 0]
    mid[0] = (p[0] + v[0])/2        # x-coordinate of midpoint
    mid[1] = (p[1] + v[1])/2        # y-coordinate of midpoint
    return mid

# Generate a large number of points
for i in range(points):
    point = new_point(point)
    x.append(point[0])
    y.append(point[1])

# Plot the results
plt.scatter(x, y, c='k', s=1)
plt.axis('Off')
plt.axes().set_aspect('equal')

x1,x2,y1,y2 = plt.axis()
plt.axis((0,1,0,.9))

plt.title("Sierpinski Triangle")
plt.savefig("sierpinski.png")
plt.show()
