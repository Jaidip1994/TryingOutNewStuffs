import numpy as np
import cv2

# Load the Image
img = cv2.imread("assets/logo.jpg", cv2.IMREAD_GRAYSCALE)
# Available mode while reading an image
# -1,   cv2.IMREAD_COLOR : Loads in color image, Any transparency of image will be neglected, its the default flag
# 0,    cv2.IMREAD_GRAYSCALE : loads an image in grayscale
# 1,    cv2.IMREAD_UNCHANGED : Loads the image as it is including the alpha channel


# Resize the image
# By Specifying the Image resolution
# img = cv2.resize(img, dsize=(700, 600))

# By using the fraction component
# when fx and fy are used this is mainly recommended to use dsize as (0,0)
img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)

# rotate the image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# To write the same into the file
cv2.imwrite("assets/new_img.jpg", img)

cv2.imshow('Logo Visual', img)
# Wait for infinite amount of time ( 0 means infinite and others meant that much amount of seconds )
cv2.waitKey(0)
# Destroy all the windows in the background so that the process execution is no interrupted
cv2.destroyAllWindows()
