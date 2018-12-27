#! /usr/bin/env python
"""
Create an atomic-level image using data from a scanning
tunneling microscope.

Leon Hostetler, Feb. 2, 2017

USAGE: stm.py
"""

from __future__ import division, print_function
import numpy as np
import pylab as pyl

# Main body of program


# Load the data from the file
data = np.loadtxt("stm.txt", float)

# Create a density plot of the data
pyl.imshow(data, origin="lower")
pyl.title("STM Image of Silicon Surface")
pyl.colorbar()  # Shows the range of colors alongside a numerical scale
pyl.savefig("silicon.png")
pyl.show()
