# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:13:28 2024

@author: Lycoris
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = len(nums)
        table = dict()


        for i in range (0,l):
            a = nums[i]
            b = target - a
            if b in table:
                return [i, table[b]]
            else:
                table[nums[i]] = i
            
            
                
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # 輸出: [0, 1] 