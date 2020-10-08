# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:20:11 2020

@author: 86131
"""

import numpy as np
import cv2
import time

time_start=time.time()

lineart = cv2.imread("7-12res100_l.png")
segment = cv2.imread("color_result_2.png")
color = cv2.imread("7-12res100_c.png")

blank_image = np.zeros((1700,1133,3), np.uint8)

colors_unique = np.unique(np.reshape(segment, (-1, 3)), axis=0)
color_num = colors_unique.shape[0]

for i in range(color_num):
    tmp = colors_unique[i]
    mask = np.all(segment == tmp[None, None], axis=2)
    color_tmp = np.median(color[mask], axis=0)
    blank_image[mask] = color_tmp
    
tr = np.minimum(blank_image,lineart)

cv2.imwrite("try3_median.png",tr)

time_end=time.time()
print('time cost',time_end-time_start,'s')