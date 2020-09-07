# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:37:17 2020

@author: 86131
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import skimage

from skimage import *
from skimage.filters import threshold_sauvola
from os import listdir 

def threshold(t, img):
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

for i in range(5):
    img = cv2.imread("try/"+str(i)+".jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    '''
    img = lap(img)
    cv2.imwrite("try/"+str(i)+".png",img)
    '''
    img = thre_sauvola(img, 7)
    skimage.io.imsave("try/"+str(i)+".png",img_as_uint(img))