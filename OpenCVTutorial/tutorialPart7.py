# Template Detection

import cv2
import numpy as np

img = cv2.imread("assets/soccerplaying.jpg", cv2.IMREAD_GRAYSCALE)
template = cv2.imread("assets/shoe.jpg", cv2.IMREAD_GRAYSCALE)
template_ball = cv2.imread("assets/ball.jpg", cv2.IMREAD_GRAYSCALE)

h, w = template.shape

h_ball, w_ball = template_ball.shape

# template matching methods
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


def fetchMatchedImagedSection(org_img, template_img, tm_method, height, width):
    # performing a convolution with the Template image on the base image
    # Result is roughly the image matching the original image
    # Dimension of the result will be (W-w+1, H-h+1)
    # W, H = dimension of the base image and (w,h) = dimension of the template image
    result = cv2.matchTemplate(org_img, template_img, tm_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if tm_method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        rec_location = min_loc
    else:
        rec_location = max_loc
    rec_bottom_right = (rec_location[0] + width, rec_location[1] + height)
    return rec_location, rec_bottom_right


for method in methods:
    img2 = img.copy()
    location, bottom_right = fetchMatchedImagedSection(img, template, method, h, w)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    location, bottom_right = fetchMatchedImagedSection(img, template_ball, method, h_ball, w_ball)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow("Match", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
