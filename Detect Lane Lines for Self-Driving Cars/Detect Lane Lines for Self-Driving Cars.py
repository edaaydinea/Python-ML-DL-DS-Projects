# Our goal is to mask the region of interest we can focus our efforts for the lane lines.
# FIRST PART
"""Mask -> Black(0)(everywhere except road) & White(255)(road)
Keeping the region of interest and masking anything else."""

# SECOND PART
""" It is how can we actually select the pixels only with their value.(Lean lines in it)
First the region of interest masking. Second step is going to do kind of pixel selection.
We're just going to select pixels only has ones in them which indicates weight.
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Read the image and display it.

image_color = mpimg.imread("image_lane_c.jpg")
print(image_color.shape)
plt.imshow(image_color)
plt.show()

# Change the color of image and show new image.
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap="gray")
print(image_gray.shape)
plt.show()

# Change the color of image.
image_copy = np.copy(image_gray)
print(image_copy.shape)
image_copy[(image_copy[:, :] < 250)] = 0  # any value that is not white color

# Display the image
plt.imshow(image_copy, cmap="gray")
plt.show()
