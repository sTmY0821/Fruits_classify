import cv2
import numpy as np
import math

im = cv2.imread("data/CPU3.png")
cv2.imshow("im",im)
im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret , im_bin = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("im_gray",im_gray)
cv2.imshow("im_bin",im_bin)

contours, hierarchy = cv2.findContours(im_bin,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
mask = np.zeros(im_bin.shape,np.uint8)
cv2.drawContours(mask,contours,-1,(255,0,0),-1)
cv2.imshow("mask",mask)

im_sub = cv2.subtract(mask,im_bin)
cv2.imshow("im_sub",im_sub)

kernel = np.ones((8,8),np.uint8)
im_close = cv2.morphologyEx(im_sub,cv2.MORPH_CLOSE,kernel,iterations=1)
cv2.imshow("im_close",im_close)

contours, hierarchy = cv2.findContours(im_close,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

(x,y),radius = cv2.minEnclosingCircle(contours[0])
center = (int(x),int(y))
radius = int(radius)
cv2.circle(im,center,radius,(255,0,0),3)
cv2.imshow("im",im)


cv2.waitKey()
cv2.destroyAllWindows()