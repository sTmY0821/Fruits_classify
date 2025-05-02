import cv2
import numpy as np

im = cv2.imread("data/3.png", 1)
cv2.imshow("original", im)


gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

im_contours = cv2.drawContours(im,contours,-1,(0,0,255),3)

cv2.imshow("contours",im_contours)

cv2.waitKey()
cv2.destroyAllWindows()