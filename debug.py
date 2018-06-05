# -*- coding: utf-8 -*-
__author__ = '樱花落舞'
import cv2
import numpy as np
import config
# 引用全局变量



def img_show(filename):
    cv2.imshow("img_show",filename)
    cv2.waitKey(0)





def img_contours(oldimg,box):
    box = np.int0(box)
    oldimg = cv2.drawContours(oldimg, [box], 0, (0, 0, 255), 2)
    cv2.imshow("img_contours", oldimg)
    cv2.waitKey(0)

def img_car(img_contours):
    pic_hight, pic_width = img_contours.shape[:2]
    return pic_hight,pic_width