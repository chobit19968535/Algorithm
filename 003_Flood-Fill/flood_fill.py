# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:19:10 2024

@author: Lycoris
"""

import numpy as np
from collections import deque

stride = 5
height = 5

img = np.zeros((height,stride))
for i in range (0, height):
    row = np.random.choice((0,1), size = stride, p =[.75, .25])
    img[i,:] = row

start_x = np.random.randint(0, stride-1)
start_y = np.random.randint(0, height-1)

X = (start_y, start_x)

while(img[X] != 0):
    start_x = np.random.randint(0, stride-1)
    start_y = np.random.randint(0, height-1)
    X = (start_y, start_x)

def Flood_fill(img, visted, start):
    queue = deque([start])
    while(queue):
        node = queue.popleft()
        if img[node] == 0:    
            print(node)
            img[node] = 2
            candicates = []
            candicates.append((node[0]-1, node[1]))
            candicates.append((node[0], node[1]-1))
            candicates.append((node[0]+1, node[1]))
            candicates.append((node[0], node[1]+1))
            
            
            for candicate in candicates:
                if candicate[0] >=0 and candicate[1]>=0:
                    if candicate[0] <height and candicate[1] < stride:
                        queue.append(candicate)
            
    
Flood_fill(img, X)