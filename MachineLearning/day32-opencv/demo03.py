import numpy as np
import cv2

#图像缩放
im = cv2.imread("data/Linus.png",1)
cv2.imshow("im",im)


h,w = im.shape[:2]

dst_size =(int(w/2),int(h/2))
resized = cv2.resize(im,dst_size)
cv2.imshow("resized",resized)

dst_size = (200,300)
im_resized = cv2.resize(im,dst_size)
cv2.imshow("im_resized",im_resized)

dst_size = (200,300)
im_resized01 = cv2.resize(im,dst_size,interpolation=cv2.INTER_NEAREST)
cv2.imshow("im_resized01",im_resized01)


dst_size = (200,300)
im_resized02 = cv2.resize(im,dst_size,interpolation=cv2.INTER_LINEAR)
cv2.imshow("im_resized02",im_resized02)

cv2.waitKey()
cv2.destroyAllWindows()

