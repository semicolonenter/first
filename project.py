#####################################################################################
# original template code
import cv2
import numpy as np

image = cv2.imread("nv0043.jpg")
# image = cv2.resize(image, (300,300))

cv2.imshow("image", image)
cv2.waitKey(0)

#####################################################################################