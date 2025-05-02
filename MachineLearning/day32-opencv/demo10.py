import cv2
import numpy as np
from cv2 import ellipse

im = cv2.imread("data/cloud.png")
cv2.imshow("im",im)

im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,im_bin = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(im_bin,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
ellipse_data = cv2.fitEllipse(contours[0])
print(ellipse_data)

cv2.ellipse(im,ellipse_data,(0,0,255),2)
cv2.imshow("im",im)

cv2.waitKey()
cv2.destroyAllWindows()