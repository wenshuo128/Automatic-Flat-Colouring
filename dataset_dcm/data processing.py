# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:37:17 2020

@author: 86131
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import skimage

from skimage import img_as_float,img_as_ubyte

from skimage import *
from skimage.filters import threshold_sauvola
from os import listdir 

def threshold(t, img):
        th_img = img.copy()
        th_img[th_img>t] = 255
        th_img[th_img<=t] = 0
        return th_img
    
def threshold_HSV(t, img):
        th_img = img.copy()
        th_img[th_img>t] = 255
        th_img[th_img<=t] = 0
        return th_img
    
def lap(img):
    img_lap = cv2.GaussianBlur(img, (3, 3), 0)
    ddepth = cv2.CV_16S
    kernel_size = 3
    img_lap = cv2.Laplacian(img_lap, ddepth, ksize=kernel_size)
    img_lap = 255 - img_lap
    '''
    plt.hist(img.ravel(), 256,[0,256])
    plt.show()
    '''
    img_lap = threshold(230, img_lap)
    return img_lap

def thre_sauvola(img, windowsize):
    thresh_sauvola = threshold_sauvola(img, window_size=windowsize)
    binary_sauvola = img > thresh_sauvola
    return binary_sauvola

def skimage2opencv(src):
    src *= 255
    src.astype(int)
    cv2.cvtColor(src,cv2.COLOR_RGB2BGR)
    return src

for i in range(5):
    img_ori = cv2.imread(f"try/{i}.jpg")
    img = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
    
    img_0 = lap(img)
    cv2.imwrite(f"Laplacian/{i}.png",img_0)
    
    img_1 = thre_sauvola(img, 21)
    img_1 = img_as_ubyte(img_1)
    cv2.imwrite(f"threshold_sauvola_21/{i}.png",img_1)
    
    img_2 = thre_sauvola(img, 17)
    img_2 = img_as_ubyte(img_2)
    cv2.imwrite(f"threshold_sauvola_17/{i}.png",img_2)
    
    img_HSV = cv2.cvtColor(img_ori, cv2.COLOR_BGR2HSV)
    img_V = cv2.split(img_HSV)[2]
    img_3 = thre_sauvola(img_V, 17)
    img_3 = img_as_ubyte(img_3)
    cv2.imwrite(f"threshold_sauvola_17_HSV/{i}.png",img_3)
    
    img_4 = thre_sauvola(img_V, 21)
    img_4 = img_as_ubyte(img_4)
    cv2.imwrite(f"threshold_sauvola_21_HSV/{i}.png",img_4)


# try global thre on HSV

'''
img = cv2.imread("try/1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

plt.hist(img[0].ravel(), 256,[0,256])
plt.show()

plt.hist(img[1].ravel(), 256,[0,256])
plt.show()

plt.hist(img[2].ravel(), 256,[0,256])
plt.show()

img_0 = cv2.inRange(img, (0, 0, 100), (255, 255, 255))

cv2.imwrite("1.png",img_0)

img_1 = thre_sauvola(img[2], 21)
skimage.io.imsave("2.png",img_as_uint(img_1))
'''

# try local thre in HSV

'''
img = cv2.imread("try/1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h=cv2.split(img)[0]
s=cv2.split(img)[1]
v=cv2.split(img)[2]
img_0 = thre_sauvola(h, 13)
img_1 = thre_sauvola(s, 13)
img_2 = thre_sauvola(v, 17)

img_0 = img_as_ubyte(img_0)
img_1 = img_as_ubyte(img_1)
img_2 = img_as_ubyte(img_2)
cv2.imwrite("h.png",img_0)
cv2.imwrite("s.png",img_1)
cv2.imwrite("v.png",img_2)
'''






















