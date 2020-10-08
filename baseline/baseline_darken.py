# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:31:01 2020

@author: 86131
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

time_start=time.time()

lineart = cv2.imread("7-12res100_l.png")
segment = cv2.imread("color_result_2.png")
color = cv2.imread("7-12res100_c.png")

dic = {}
count = 0

for i in range(1700):
    for j in range(1133):
        if dic.get(str(segment[i,j]), -1) == -1:
            dic[str(segment[i,j])] = count
            count = count + 1

blank_image = np.zeros((1700,1133,3), np.uint8)

parts = [[] for _ in range(count)]
color_template = [[0,0,0] for _ in range(count)]

for i in range(1700):
    for j in range(1133):
        parts[dic[str(segment[i,j])]].append(color[i,j])
        
for i in range(count):
    tmp = len(parts[i])
    for j in range(tmp):
        color_template[i][0] = color_template[i][0] + parts[i][j][0]
        color_template[i][1] = color_template[i][1] + parts[i][j][1]
        color_template[i][2] = color_template[i][2] + parts[i][j][2]
    color_template[i][0] = color_template[i][0] // tmp
    color_template[i][1] = color_template[i][1] // tmp
    color_template[i][2] = color_template[i][2] // tmp


for i in range(1700):
    for j in range(1133):
        blank_image[i,j,0] = min(color_template[dic[str(segment[i,j])]][0],lineart[i,j,0])
        blank_image[i,j,1] = min(color_template[dic[str(segment[i,j])]][1],lineart[i,j,1])
        blank_image[i,j,2] = min(color_template[dic[str(segment[i,j])]][2],lineart[i,j,2])
        
cv2.imwrite("final_result_darken_2.png",blank_image)
time_end=time.time()
print('time cost',time_end-time_start,'s')
'''
for i in range(1700):
    for j in range(1133):
        if lineart[i,j,0]+lineart[i,j,1]+lineart[i,j,2] < 253:
            blank_image[i,j,0] = lineart[i,j,0]
            blank_image[i,j,1] = lineart[i,j,1]
            blank_image[i,j,2] = lineart[i,j,2]
        else:
            blank_image[i,j,0] = color_template[dic[str(segment[i,j])]][0]
            blank_image[i,j,1] = color_template[dic[str(segment[i,j])]][1]
            blank_image[i,j,2] = color_template[dic[str(segment[i,j])]][2]

        
cv2.imwrite("final_result_3.png",blank_image)
'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        