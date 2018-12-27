#! /usr/bin/env python
"""
Display an animation of the solar system including the inner
planets as well as Jupiter and Saturn.

Leon Hostetler, Feb. 9, 2017

USAGE: solar_system.py
"""

from __future__ import division, print_function
from visual import sphere, color, rate, shapes, extrusion, local_light, scene, materials
import numpy as np

c1 = 1500   # Radius multiplier
c2 = 50     # Rate

# Create the sun
sphere(pos=(0, 0, 0), radius=1e7, material=materials.emissive, color=color.yellow)

# Make the sun the light source
scene.lights = []  # Turn off the ambient lighting
lamp = local_light(pos=(0, 0, 0), color=color.yellow)

# Columns are: radius (km), orbital radius (km), and orbital period.
planetData = np.array([[2.4400e3, 5.7900e7, 88.0],
                       [6.0520e3, 1.0820e8, 224.7],
                       [6.3710e3, 1.4960e8, 365.3],
                       [3.3860e3, 2.2790e8, 687.0],
                       [6.9173e4, 7.7850e8, 4331.6],
                       [5.7316e4, 1.4334e9, 10759.2]], dtype=float)

# RGB values for the planet colors
colors = np.array([[0.59, 0.57, 0.50],
                   [1.00, 1.00, 0.54],
                   [0.38, 0.76, 0.97],
                   [0.87, 0.45, 0.16],
                   [1.00, 0.60, 0.00],
                   [1.00, 0.78, 0.00]], dtype=float)

# Initialize the planets.
planets = np.empty(6, sphere)
for i in range(6):
    planets[i] = sphere(pos=[planetData[i, 1], 0, 0],
                        color=(colors[i, 0], colors[i, 1], colors[i, 2]),
                        radius=c1*planetData[i, 0],
                        make_trail=True)

# Make Saturn's ring system
outer = shapes.circle(pos=(0,1.5), radius=planetData[5, 0]*c1*2)
inner = shapes.circle(pos=(0,1.5), radius=planetData[5, 0]*c1*1.3)
location = [planets[5].pos, (planets[5].pos[0], planets[5].pos[1], planets[5].pos[2]+1000)]
saturnsRings = extrusion(pos=location,
                         shape=outer-inner,
                         color=(1, 0.78, 0))


def increment_planet(p):
    """
    This function increments the position of planet p by obtaining its current
    position and then calculating its new position after taking the planet's
    orbital period into account.
    """
    x = planets[p].pos[0]  # Current x coordinate
    y = planets[p].pos[1]  # Current y coordinate
    angle = np.arctan2(y, x)
    radius = planetData[p, 1]
    period = planetData[p, 2]
    newAngle = angle + (2*np.pi)/period
    X = radius*np.cos(newAngle)
    Y = radius*np.sin(newAngle)
    planets[p].pos = [X, Y, 0]


while True:
    rate(c2)
    for i in range(len(planets)):
        increment_planet(i)
    saturnsRings.pos = planets[5].pos
