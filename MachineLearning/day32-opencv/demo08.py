import numpy as np
import cv2

im = cv2.imread("data/lena.jpg", 1)
cv2.imshow("original", im)

im_median_blur = cv2.medianBlur(im, 5)
cv2.imshow("median_blur", im_median_blur)

im_mean_blur = cv2.blur(im, (3, 3))
cv2.imshow("mean_blur", im_mean_blur)

im_gaussian_blur = cv2.GaussianBlur(im, (5, 5), 3)
cv2.imshow("gaussian_blur", im_gaussian_blur)

gaussan_blur = np.array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4]
    , [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4, 7, 4, 1]
    ], np.float32) / 273
im_gaussian_blur2 = cv2.filter2D(im, -1, gaussan_blur)
cv2.imshow("gaussian_blur2", im_gaussian_blur2)

cv2.waitKey()
cv2.destroyAllWindows()
