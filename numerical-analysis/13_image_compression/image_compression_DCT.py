#! /usr/bin/env python
"""
Image compression with the discrete cosine transform.

Leon Hostetler, Apr. 14, 2017

USAGE: python image_compression_DCT.py

"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
import numpy as np


def DCT(block, N=8):
    """Perform the DCT on an 8 x 8 square block and return the result."""

    if block.shape != (N, N):
        raise ValueError("Input block to DCT is wrong size!")

    blockDCT = np.zeros([N, N])

    piN = np.pi/N
    a1 = np.sqrt(1/N)
    a2 = np.sqrt(2/N)

    for p in range(N):
        for q in range(N):

            if p == 0:
                alphap = a1
            else:
                alphap = a2
            if q == 0:
                alphaq = a1
            else:
                alphaq = a2

            alphas = alphap*alphaq

            pN, qN = p*piN, q*piN
            for m in range(N):
                for n in range(N):
                    cosines = np.cos(pN*(m + 0.5))*np.cos(qN*(n + 0.5))
                    blockDCT[p, q] += alphas*block[m, n]*cosines

    return blockDCT


def inv_DCT(block, K, N=8):
    """Perform the inverse DCT on an 8 x 8 square block and return the result."""

    if block.shape != (N, N):
        raise ValueError("Input block to inv_DCT is wrong size!")

    invBlockDCT = np.zeros([N, N])
    b = np.sqrt(1/2)

    for p in range(N):
        for q in range(N):
            ppi = np.pi*(p+0.5)/N
            qpi = np.pi*(q+0.5)/N
            for m in range(K):
                cosm = np.cos(m * ppi)
                for n in range(K):
                    if m == 0:
                        betam = b
                    else:
                        betam = 1
                    if n == 0:
                        betan = b
                    else:
                        betan = 1
                    invBlockDCT[p, q] += betam*betan*block[m, n]*cosm*np.cos(n*qpi)
            invBlockDCT[p, q] *= 2/N

    invBlockDCT = invBlockDCT.astype('uint8')

    return invBlockDCT


# Create an array in which each element is an 8x8x1 block that has had
# the DCT applied to it

#####################################################################
# Import and check image
#####################################################################

# Size of the DCT blocks
N = 8

# Import the image as an array
pic = ndimage.imread('koala.jpg', mode='RGB')

# NOTE: If image dimensions are not divisible by N, the image is cropped
# in this process.

#####################################################################
# Chop image into N x N blocks
#####################################################################

# Create a list to store the blocks after the DCT has been applied
# Blocks are stored in the list in the following order. First element
# of list is the DCT of the 8x8x1 block in the top-left corner of the
# image. The next elements are the remaining blocks in the top row of the
# first (i.e. third index = 0) slice of the image. After that, the remaining
# rows of blocks in the first slice from top to bottom. After the first
# slice is completed, the process is repeated with the remaining two slices.

# Dimensions of imported picture
rows = int(pic.shape[0])    # Number of rows in pixels
cols = int(pic.shape[1])    # Number of columns in pixels
depth = int(pic.shape[2])   # Number of layers in pixels (3 for RGB images)

bR = int(cols/N)            # Width of image in terms of NxN blocks
rS = int(rows/N)            # Height of image in terms of NxN blocks

pic_blocks = []             # List of N x N blocks
for layer in range(depth):
    for row in range(rS):
        for col in range(bR):
            currentBlock = pic[row*N:row*N+N, col*N:col*N+N, layer]
            pic_blocks.append(currentBlock)

#####################################################################
# Take DCT of each image block
#####################################################################

pic_blocks_DCT = []
for block in pic_blocks:
    pic_blocks_DCT.append(DCT(block))

#####################################################################
# Take inverse DCT of each block (i.e. compress the image)
#####################################################################

# Take the inverse DCT of all the blocks in pic_DCT
# Set second parameter in inv_DCT() to < N to compress the image
# Set parameter = N for no compression
pic_blocks_iDCT = []
for block in pic_blocks_DCT:
    pic_blocks_iDCT.append(inv_DCT(block, 2))

#####################################################################
# Reconstruct the image from the blocks in pic_blocks_iDCT
#####################################################################

layers = []
for k in range(depth):

    rowsInLayer = []
    for i in range(k*rS, (k+1)*rS):
        rowsInLayer.append(np.hstack(pic_blocks_iDCT[i * bR:(i + 1) * bR]))

    layers.append(np.vstack(rowsInLayer))

# Stack the 3 layers together
compressed_pic = np.dstack(layers)

#####################################################################
# Save and display the results
#####################################################################

misc.imsave('compressed.png', compressed_pic)

plt.figure(1)
plt.subplot(121)
plt.title("Original Image")
plt.axis('off')
plt.imshow(pic)

plt.subplot(122)
plt.imshow(compressed_pic)
plt.title("Compressed Image")
plt.axis('off')
plt.show()
