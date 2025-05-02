import numpy as np
import cv2

im = cv2.imread("data/6.png", 1)
cv2.imshow("im", im)

kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(im, kernel, iterations=5)
cv2.imshow("dilate", dilate)
cv2.waitKey()
cv2.destroyAllWindows()