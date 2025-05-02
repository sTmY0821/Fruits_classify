import numpy as np
import cv2

im = cv2.imread("data/5.png", 1)
cv2.imshow("im", im)
kernel = np.ones((5, 5), np.uint8)#3*3的核，值全为1，类型为8bits无符号int
im_erode = cv2.erode(im, kernel,iterations=1)
cv2.imshow("im_erode", im_erode)

cv2.waitKey()
cv2.destroyAllWindows()