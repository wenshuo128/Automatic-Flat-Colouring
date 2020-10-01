# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:31:01 2020

@author: 86131
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

lineart = cv2.imread("lineart.png")

segment = cv2.imread("segment_region.png")
#print(segment[300,300])
color = cv2.imread("result_from_ADP.png")

dic = {}
#dic[str(color[2,2])]=1
#print(str(dic))

count = 0

for i in range(512):
    for j in range(512):
        if dic.get(str(segment[i,j]), -1) == -1:
            dic[str(segment[i,j])] = count
            count = count + 1

blank_image = np.zeros((512,512,3), np.uint8)

parts = [[] for _ in range(count)]
color_template = [[0,0,0] for _ in range(count)]

for i in range(512):
    for j in range(512):
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
    
for i in range(512):
    for j in range(512):
        if lineart[i,j,0]+lineart[i,j,1]+lineart[i,j,2] < 253:
            blank_image[i,j,0] = lineart[i,j,0]
            blank_image[i,j,1] = lineart[i,j,1]
            blank_image[i,j,2] = lineart[i,j,2]
        else:
            blank_image[i,j,0] = color_template[dic[str(segment[i,j])]][0]
            blank_image[i,j,1] = color_template[dic[str(segment[i,j])]][1]
            blank_image[i,j,2] = color_template[dic[str(segment[i,j])]][2]

        
cv2.imwrite("final_result.png",blank_image)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        