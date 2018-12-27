#! /usr/bin/env python
"""
Takes the speed traveled by a spacecraft and the distance
to travel as inputs and returns the trip time as measured from Earth and
as measured by a passenger.

Leon Hostetler, Jan. 22, 2017

USAGE: python special_relativity.py

"""
from __future__ import division, print_function


x = float(raw_input("Enter the distance to the planet (light years): "))
v = float(raw_input("Enter the speed of the rocket (fraction of c): "))

# Trip time from Earth's perspective
t1 = x/v

# Trip time from passenger's perspective
t2 = t1*(1 - v**2)**(1/2)

# Print results
print("The trip time from Earth's perspective is ", t1, " years.")
print("The trip time from a passenger's perspective is ", t2, " years.")
