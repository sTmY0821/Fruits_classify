import cv2
import numpy as np
import math

im = cv2.imread("data/paper.jpg")
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
w,h = gray_im.shape
cv2.imshow("im", im)

blurred = cv2.GaussianBlur(gray_im, (5, 5), 0)
dilate = cv2.dilate(blurred, (3, 3))
edged = cv2.Canny(dilate, 30, 120)
cv2.imshow("edged", edged)

cnts, hie = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

im_cnt = cv2.drawContours(im, cnts, -1, (0, 0, 255), 3)

cv2.imshow("im_cnt", im_cnt)

docCnt = None
if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            docCnt = approx
            break
print(docCnt)

points = []
for peak in docCnt:
    peak = peak[0]
    cv2.circle(im, tuple(peak), 10, (0, 0, 255), 2)
    points.append(peak)

print(points)
cv2.imshow("im_point", im)

src = np.float32([points[0], points[1], points[2], points[3]])
h = int(math.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2))
w = int(math.sqrt((points[2][0] - points[1][0]) ** 2 + (points[2][1] - points[1][1]) ** 2))
dst = np.float32([[0, 0], [0, h], [w, h], [w, 0]])
m = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(im, m, (w, h))
cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()
