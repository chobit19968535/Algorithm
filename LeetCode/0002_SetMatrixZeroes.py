# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:35:24 2025

@author: Dino
"""
import math

matrix = [[1,0]]


stride = len(matrix[0])
height = len(matrix)

cells = stride * height

zeros = list()
list_hor = list()
list_ver = list()


for i in range(cells):
    y = (int)(math.floor((i/stride)))
    x = i%stride
    if(matrix[y][x] == 0):
        zeros.append(i)
        if x not in list_ver:
            list_ver.append(x)
        if y not in list_hor:
            list_hor.append(y)


for i in list_ver:
    x = i
    y = 0
    while(True):
        if ( y >= height  ):
            break
        else:
            matrix[y][i] = 0
            y = y+1
            
for i in list_ver:
    x = i
    y = height-1
    while(True):
        if ( y < 0  ):
            break
        else:
            matrix[y][i] = 0
            y = y-1
            
for i in list_hor:
    y = i
    x = stride-1
    while(True):
        if ( x < 0  ):
            break
        else:
            matrix[y][x] = 0
            x = x-1
            
for i in list_hor:
    y = i
    x = 0
    while(True):
        if ( x >= stride  ):
            break
        else:
            matrix[y][x] = 0
            x = x+1