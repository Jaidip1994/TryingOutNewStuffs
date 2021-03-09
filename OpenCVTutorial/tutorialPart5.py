# Colors and color detection

# HSV: Hue Saturation and Lightness / Brightness
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # conversion of bgr to hsv mode is required because the method later will need the image in that format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # For the color selection, there is a need to get the lower bound and also upper bound
    # Both the bounds value has to be provided in HSV format

    # Hence the one way is to create an image which has only one pixel and then covert the BGR to HSV
    # BGR_color = np.array([[[255, 0, 0]]])
    # cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)

    # Other way to get the corresponding HSV Value of the color
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Mask basically returns the pixels which falls in this range( in range as 1 and out of range as 0 )
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("Result", result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
