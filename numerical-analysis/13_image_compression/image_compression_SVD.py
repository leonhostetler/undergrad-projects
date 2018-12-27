#! /usr/bin/env python
"""
Image compression using singular value decomposition.

Leon Hostetler, Apr. 9, 2017

USAGE: python image_compression_SVD.py

"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
import numpy as np


# Import the image as an array
pic = ndimage.imread('face.png', mode='RGB')

print(pic.shape)

# Break image array into three layers
layer1 = pic[:, :, 0]
layer2 = pic[:, :, 1]
layer3 = pic[:, :, 2]

# Compute SVD of each layer
# The s's are lists containing the ordered singular values
U1, s1, Vt1 = np.linalg.svd(layer1, full_matrices=False)
U2, s2, Vt2 = np.linalg.svd(layer2, full_matrices=False)
U3, s3, Vt3 = np.linalg.svd(layer3, full_matrices=False)

# What fraction of the singular values should be kept?
keep = .02
s1[int(len(s1)*keep):] = 0.0
s2[int(len(s1)*keep):] = 0.0
s3[int(len(s1)*keep):] = 0.0

# Compute the new layers
new_layer1 = np.dot(U1, np.dot(np.diag(s1), Vt1))
new_layer2 = np.dot(U2, np.dot(np.diag(s2), Vt2))
new_layer3 = np.dot(U3, np.dot(np.diag(s3), Vt3))

# Recombine the layers
new_pic = np.dstack([new_layer1, new_layer2, new_layer3])

# Save/export the new image
misc.imsave('compressed_SVD.png', new_pic)

# Re-import the saved image to display in graph. For some reason
# plt.imshow is having trouble displaying new_pic even though
# misc.imsave has no trouble exporting the image
newest_pic = ndimage.imread('compressed_SVD.png', mode='RGB')

# Display the results
plt.figure(1)
plt.subplot(121)
plt.title("Original Image")
plt.axis('off')
plt.imshow(pic)

plt.subplot(122)
#plt.imshow(new_pic)
plt.imshow(newest_pic)
plt.title("Compressed Image")
plt.axis('off')
plt.show()
