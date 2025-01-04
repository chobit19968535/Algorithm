# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:35:24 2025

@author: Dino
"""
import math

matrix = [[1,1,1],[1,0,1],[1,1,1]]

stride = len(matrix[0])
height = len(matrix)

cells = stride * height

zeros = list()

for i in range(cells):
    y = math.floor((i/stride))
    x = i%stride
    if(matrix[y][x] == 0):
        zeros.append(i)

