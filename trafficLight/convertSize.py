import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = cv2.imread('test7.jpg')
plt.imshow(img)
# plt.show()
size = (960, 540)
halfImg = cv2.resize(img, size)
plt.imshow(halfImg)
# plt.show()
cv2.imwrite('test8.jpg', halfImg)
