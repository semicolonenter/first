#####################################################################################
# original template code
import cv2
import numpy as np

image = cv2.imread("images/group1.jpg")

cv2.imshow("image", image)
cv2.waitKey(0)

#####################################################################################

# convert to gray-scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# CLAHE contrast enhancement
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
image_clahe = clahe.apply(gray)



