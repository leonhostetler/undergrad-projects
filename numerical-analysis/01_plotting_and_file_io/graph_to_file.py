#! /usr/bin/env python
"""
  This basic program outputs the x and y values from two different functions
  into text files so they can be plotted later.

  Leon Hostetler
  Jan. 14, 2017

  USAGE: python graph_to_file.py

"""
from __future__ import division, print_function
import numpy as np

# Define the variables
a = 0
b = 2*np.pi
N = 100  # Upper limit

#
# Define the functions
#


def f(x):
    return np.cos(x)


def g(x):
    if x < np.pi:
        return -1
    else:
        return 1


#
#  This part writes to the text files. If the file doesn't exist, it is
#  automatically created. If it does exist, its contents are overwritten.
#

with open("datafile1.txt", "w") as text_file:
    for i in range(0, N+1):
        x_i = a + ((b-a)/N)*i
        text_file.write(str(x_i) + '\t' + str(f(x_i)) + '\n')

with open("datafile2.txt", "w") as text_file:
    for i in range(0, N+1):
        x_i = a + ((b-a)/N)*i
        text_file.write(str(x_i) + '\t' + str(g(x_i)) + '\n')
