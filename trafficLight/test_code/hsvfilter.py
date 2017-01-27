import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# img = cv2.imread('test12.jpg')
# img = cv2.imread('test3.jpg')  # white test
img = cv2.imread('test7.jpg')  # yellow test
# plt.imshow(img)
# plt.show()

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV RGB? BGR? R255 G255
lower_yellow = np.array([0, 100, 100], dtype=np.uint8)  # x 254 200 70
upper_yellow = np.array([100, 255, 255], dtype=np.uint8)
# Threshold the HSV image to get only yellow colors 120 166 200
mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)

# define range of blue color in HSV
lower_white = np.array([220, 220, 220], dtype=np.uint8)
upper_white = np.array([255, 255, 255], dtype=np.uint8)
# Threshold the HSV image to get only white colors
mask2 = cv2.inRange(img, lower_white, upper_white)

# Bitwise - AND mask and original image

res1 = cv2.bitwise_and(img, img, mask=mask1)
res2 = cv2.bitwise_and(img, img, mask=mask2)
res3 = cv2.bitwise_or(res1, res2)

#cv2.imshow('img', img)
#cv2.imshow('mask', mask1)
#cv2.imshow('res', res)
# k = cv2.waitKey(5) & 0xFF
# if k == 27:
#    break

cv2.imwrite('test_mask1.jpg', res1)
cv2.imwrite('test_mask2.jpg', res2)
cv2.imwrite('test_mask3.jpg', res3)
