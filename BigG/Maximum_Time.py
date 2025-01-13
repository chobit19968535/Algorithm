# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:12:49 2025

@author: Lycoris
"""


import random 

if(random.randint(0,1)):
    x0 = (random.randint(0,2))
else:
    x0 = "?"
    

if(random.randint(0,1)):
    x1 = (random.randint(0,9))
else:
    x1 = "?"
    

if(random.randint(0,1)):
    x2 = (random.randint(0,5))
else:
    x2 = "?"
    
if(random.randint(0,1)):
    x3 = (random.randint(0,9))
else:
    x3 = "?"
    
puzzle = [x0, x1, ":", x2, x3]
puzzle_ = [x0, x1, ":", x2, x3]

seconds = 24*60*60-1

if(puzzle[4] =='?'):
    puzzle[4] = 9


if(puzzle[3] =='?'):
    puzzle[3] = 5
    
secs = (int)( (str)(puzzle[3]) + (str)(puzzle[4]))*60
remain = seconds - secs


if(puzzle[1] !='?' and puzzle[0] == '?' ):
    for i in range(2, -1, -1):
        if (int)(str(i) + (str)(puzzle[1]))*3600 <= remain:
            puzzle[0] = str(i)
            break
        
if(puzzle[0] !='?' and puzzle[1] == '?' ):
    for i in range(9, -1, -1):
        if (int)(str(puzzle[0]) + str(i))*3600 <= remain:
            puzzle[1] = str(i)
            break
        
if(puzzle[0] == '?' and puzzle[1] == '?'):
    puzzle[0] =  2
    puzzle[1] =  3
res = ""
for i in puzzle:
    res = res + str(i)
print(res)
