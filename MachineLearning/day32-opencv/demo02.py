import numpy as np
import cv2

#仿射变换：旋转、缩放、平移、镜像

def translate(img,x,y):
    """
    图像平移
    :param img:原图
    :param x: 水平方向移动的像素
    :param y: 垂直方向移动的像素
    :return: 经过平移后的图像
    """
    h,w = img.shape[:2]
    M = np.float32([[1,0,x],[0,1,y]])
    #进行仿射变换
    dsty = cv2.warpAffine(img,M,(w,h))
    return dsty

def rotate(img,angle,center=None,scale=1.0):
    """
    图像旋转
    :param img: 原图
    :param angle: 旋转角度
    :param center: 旋转中心
    :param scale: 缩放比例
    :return: 经过旋转后的图像
    """
    (h,w) = img.shape[:2]
    if center is None:
        center = (w//2,h//2)
    #进行旋转
    M = cv2.getRotationMatrix2D(center,angle,scale)#返回一个旋转矩阵
    dst = cv2.warpAffine(img,M,(w,h))
    return dst


if __name__ =="__main__":
    im = cv2.imread("data/lena.jpg",1)
    cv2.imshow("im",im)
    im_shifted = translate(im,100,100)
    cv2.imshow("im_shifted",im_shifted)
    # 逆时针旋转45度
    rotated = rotate(im, 45)
    cv2.imshow("rotated1", rotated)
    # 顺时针旋转180度
    rotated = rotate(im,-90)
    cv2.imshow("rorated2", rotated)



    cv2.waitKey()
    cv2.destroyAllWindows()