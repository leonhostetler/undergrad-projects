#! /usr/bin/env python
"""
Uses VPython to show a 3D model of the lattice structure of NACl.

Leon Hostetler, Feb. 3, 2017

USAGE: python lattice_nacl.py
"""
from __future__ import division, print_function
from visual import *

L = 5
R = 0.5

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if (i + j + k)%2 == 0:
                sphere(pos=[i, j, k], radius=R, color=color.red)
            else:
                sphere(pos=[i, j, k], radius=R, color=color.blue)


