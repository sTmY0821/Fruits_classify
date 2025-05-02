import numpy as np
import cv2


def random_crop(im,w,h):
    start_x = np.random.randint(0,im.shape[1])
    start_y = np.random.randint(0,im.shape[0])
    new_img = im[start_y:start_y+h,start_x:start_x+w]
    return new_img

def center_crop(im,w,h):
    start_x = int(im.shape[1]/2)-int(w/2)
    start_y = int(im.shape[0]/2)-int(h/2)
    new_img = im[start_y:start_y+h,start_x:start_x+w]
    return new_img