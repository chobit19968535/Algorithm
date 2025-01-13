# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:16:24 2025

@author: Dino
"""

keyboard = "abcdefghijklmnopqrstuvwxyz"

text = "cba" 


cnt = ord(text[0]) - ord('a')
for i in range(1, len(text)):
    cnt = cnt +  abs(ord(text[i])  - ord(text[i-1]))