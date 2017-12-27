# *************************************************
# * WRITEN BY VARZERO                             *
# * DATE 2017/12/21                               *
# * AR디바이스 UI 및 음성인식, 사물인식의 메인             *
# * LA_Ch_*()                                     *
# *************************************************

import cv2

def LA_Ch_ImageInit(img):
    return cv2.imread(img)

def LA_Ch_ColorGray(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)