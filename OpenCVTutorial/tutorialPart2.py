import cv2
import random

img = cv2.imread("assets/logo.jpg", cv2.IMREAD_COLOR)

# cv2 is having the data represented in numpy array format
print(type(img))
print(img.shape)

print(img[250][45:400])

# Image manipulation with some random values
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# cv2.imshow('Enhanced Image Visualize', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Image Cropping ( in the below example its trying to extract the logo out of the image )
# and then paste it on to the same image
tag = img[100:450, 450:830]
img[350:700, 150:530] = tag

cv2.imshow('Extracted Image Visualize', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
