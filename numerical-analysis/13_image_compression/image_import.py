#! /usr/bin/env python
"""
Import/export images as arrays.

Leon Hostetler, Apr. 2, 2017

USAGE: python image_import.py

"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

# Import image as array
f = misc.face()
misc.imsave('face.png', f)

# Print info about image array
print(f.shape)
print(f.dtype)

# Display image
plt.imshow(f)
plt.show()

# face.png is a color picture, so it is basically three 768x1024
# images stacked together. Separate those stacks to look at them
# individually.
slice1 = f[:, :, 0]
slice2 = f[:, :, 1]
slice3 = f[:, :, 2]

print(slice1.shape)

plt.imshow(slice1)
plt.show()
plt.imshow(slice2)
plt.show()
plt.imshow(slice3)
plt.show()

# Get the first 8x8 block in the first slice
block1 = f[0:8, 0:8, 0]

plt.imshow(block1)
plt.show()

# Save the block as an image
misc.imsave('block1.jpg', block1)
