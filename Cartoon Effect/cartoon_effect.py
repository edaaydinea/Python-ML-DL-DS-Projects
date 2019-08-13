import cv2
import matplotlib.pyplot as plt

color_image = cv2.imread("Trudeau.jpg")

"""
Stylization aims to produce digital imagery with a wide variety of effects not focused on 
photo realism. Stylization can abstract regions of low contrast while preserving, or enhancing,
high-contrast features. 

Parameters
- src Input 8-bit 3-channel image
- dst Output Image with the same size and type as src
- sigma_s Range between 0 to 200
- sigma_r Range between 0 to 1

Note
- sigma_s controls how much the image is smoothed- the larger its value, the more
smoothed the image gets, but it's also slower to compute.
- sigm_r is important if you want to preserve edges while smoothing the image.Small
sigma_r results in only very similar colors to be averaged, while colors
that differ much will stay intact.
"""
cartoon_image = cv2.stylization(color_image, sigma_s=200, sigma_r=0.3)

cv2.imshow("cartoon", cartoon_image)
cv2.waitKey()
cv2.destroyAllWindows()