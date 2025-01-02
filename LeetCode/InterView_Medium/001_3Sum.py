# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:11:23 2025

@author: Lycoris
"""

dc = dict()
nums = [-1,0,1,2,-1,-4]
l = len(nums)
for i in nums:
    if i not in dc:
        dc[i] = 1
    else:
        dc[i] = dc[i]+1
        

for z in dc:
    for i in range(0, l):
        