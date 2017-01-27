print('hoge')

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

import numpy as np

import cv2

img = cv2.imread('test8.jpg')
# plt.imshow(img)
# plt.show()

xsize = 960
ysize = 540
x1, y1 = (0, ysize - 40)
x2, y2 = (xsize / 2 - 30, 330)
x3, y3 = (xsize / 2 + 30, 330)
x4, y4 = (xsize, ysize - 40)
pts = np.array(
    [[(x1, y1), (x2, y2), (x3, y3), (x4, y4)]], dtype=np.int32)
pts = pts.reshape((-1, 1, 2))

#cv2.fillConvexPoly(img, vertices, 4)
cv2.polylines(img, [pts], True, (0, 255, 255), 4)

#size = (960, 540)
#halfImg = cv2.resize(img, size)
plt.imshow(img)
# plt.show()
cv2.imwrite('test9.jpg', img)
