# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:20:11 2020

@author: 86131
"""

import numpy as np
import cv2
import time

color = cv2.imread("7-13res100_c.png")
colors_unique = np.unique(np.reshape(color, (-1, 3)), axis=0)
color_num = colors_unique.shape[0]
print(color_num)
'''
time_start=time.time()

lineart = cv2.imread("7-13res100_l.png")
segment = cv2.imread("color_result_3.png")
color = cv2.imread("fake3.png")

blank_image = np.zeros((1700,1133,3), np.uint8)

colors_unique = np.unique(np.reshape(segment, (-1, 3)), axis=0)
color_num = colors_unique.shape[0]

'''
'''
for i in range(color_num):
    print("i:",i)
    tmp = colors_unique[i]
    mask = np.all(segment == tmp[None, None], axis=2)
    color_tmp = np.median(color[mask], axis=0)
    blank_image[mask] = color_tmp
'''
'''

for i in range(color_num):
    print("i:",i)
    tmp = colors_unique[i]
    mask = np.all(segment == tmp[None, None], axis=2)
    mask_int8 = np.int8(mask)
    ret, labels = cv2.connectedComponents(mask_int8)
    if ret > 2:
        print("ret:",ret)
        for j in range(ret-1):
            #test = np.ones((1700,1133)) * (j+1)
            mask_tmp = (labels == j+1)     
            print(mask_tmp)
            print(mask_tmp.shape)
            color_tmp = np.median(color[mask_tmp], axis=0)
            blank_image[mask_tmp] = color_tmp
    else:
        color_tmp = np.median(color[mask], axis=0)
        blank_image[mask] = color_tmp
        
tr = np.minimum(blank_image,lineart)

cv2.imwrite("fake_result_3.png",tr)

time_end=time.time()
print('time cost',time_end-time_start,'s')
'''