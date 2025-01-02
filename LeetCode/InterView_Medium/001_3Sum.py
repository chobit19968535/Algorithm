# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:11:23 2025

@author: Lycoris
"""

nums = [-1,0,1,2,-1,-4]

res = []
nums.sort()
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    seen = set()
    for j in range(i+1, len(nums)):
        complement = -nums[i] - nums[j]
        if complement in seen:
            res.append([nums[i], nums[j], complement])
        seen.add(nums[j])