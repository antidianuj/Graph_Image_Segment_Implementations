# inroder to utilize line#2, run "pip install felzenszwalb_segmentation"

from felzenszwalb_segmentation import segment
import cv2


in_image=cv2.imread("input.jpg");

sigma=0.8
k=300

min_size=50

segmented_image = segment(in_image, sigma, k, min_size)

cv2.imwrite('output.jpg',segmented_image)