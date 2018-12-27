#! /usr/bin/env python
"""
  This basic program retrieves plot data from a pair of text files and plots them.

  Leon Hostetler
  Jan. 22, 2017

  USAGE: python graph_to_file.py

  NOTE: Run file graph_to_file.py first to generate the text files.

"""
from __future__ import division, print_function
import matplotlib.pyplot as plt

#
# Data from first file
#
with open("datafile1.txt", 'r') as f:  # Get data from file as list
    content = f.read().replace('\t', '\n').splitlines()  # Strip out newlines and tabs
f.close()
x1 = content[::2]    # Get every other element
y1 = content[1::2]   # Get every other element starting with 2

#
# Data from second file
#
with open("datafile2.txt", 'r') as f:
    content = f.read().replace('\t', '\n').splitlines()
f.close()
x2 = content[::2]
y2 = content[1::2]

#
# Plot the two on a single graph
#

fig, ax = plt.subplots()
ax.plot(x1, y1, linestyle='dashed')
ax.plot(x2, y2)
ax.grid()
axes = plt.gca()
left, right, bottom, top = plt.axis()
plt.axis((left, right, bottom - 0.3, top + 0.3))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()
