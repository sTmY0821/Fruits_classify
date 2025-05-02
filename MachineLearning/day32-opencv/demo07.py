import numpy as np
import cv2

im1 = cv2.imread('data/7.jpg')
im2 = cv2.imread('data/8.jpg')

kernel = np.ones((10,10),np.uint8)

r1 = cv2.morphologyEx(im1,cv2.MORPH_OPEN,kernel)
r2 = cv2.morphologyEx(im2,cv2.MORPH_OPEN,kernel)
cv2.imshow("im1",im1)
cv2.imshow('r1',r1)
cv2.imshow("im2",im2)
cv2.imshow('r2',r2)

cv2.waitKey()
cv2.destroyAllWindows()