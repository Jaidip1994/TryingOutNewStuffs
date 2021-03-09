# Corner Detection
# shi-tomashi

import numpy as np
import cv2

img = cv2.imread("assets/Chess_Board.png")
img = cv2.resize(img, (0, 0), fx=0.8, fy=0.7)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# maxCorners is the number of corners
# qualitylevel is the Minimum quality the value ranged between 0-1
# minimumDistance is the minimum euclidean distance between the two corners

corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), thickness=-1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, thickness=1)

cv2.imshow("Frame", img)
cv2.imwrite("assets/final_output.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
