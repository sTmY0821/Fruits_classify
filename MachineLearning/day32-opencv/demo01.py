import cv2
import numpy as np

im = cv2.imread("data/opencv2.png",1)

print(im.shape)
# cv2.imshow("im",im)
# b = im[:,:,0]
# cv2.imshow("b",b)
# im.ravel()
#
# cv2.waitKey()
# cv2.destroyWindow()