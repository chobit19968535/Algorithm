# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:11:23 2025

@author: Lycoris
"""

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

# res = []
# nums.sort()

# for i in range(len(nums)):
#     if i > 0 and nums[i] == nums[i-1]:
#         continue
#     seen = set()
#     for j in range(i+1, len(nums)):
#         complement = -nums[i] - nums[j]
#         if complement in seen:
#             res.append([nums[i], nums[j], complement])
#         seen.add(nums[j])


nums.sort()
res = []
visted_z = list()

for z in range(0, len(nums)):
    # if z > 0 and nums[z-1] == nums[z]:
    #     continue
    # if nums[z] in visted_z: 
    #     continue
    visted_z.append(nums[z])
    x = 0
    y = len(nums)-1
    
    while(x<y):
        if(nums[x] + nums[y]) == -nums[z]:
            if(x !=y and x != z and y!=z):
                ans = [nums[x], nums[y], nums[z]]
                ans.sort()
                if(ans not in res):
                    res.append(ans) 
                break
            else:
                x = x +1
        if (nums[x] + nums[y]) > -nums[z]:
            y = y -1
        if (nums[x] + nums[y] ) < -nums[z]:
            x = x +1
        
        