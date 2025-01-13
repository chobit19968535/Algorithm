# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:21:19 2025

@author: Dino
"""

import random 
        
max_floors = 10
max_rooms = 26
test_length = 5555
busy_cnts = 0
LOG = list()

for i in range(0, test_length):
    idle = False
    if(random.randint(0,1)): idle  = True
    floor = random.randint(0,9)
    room = random.randint(0,26) + 65
    room = chr(room)
    if(idle):
        LOG.append("+"+(str)(floor) +(str)(room) )
    else:
        LOG.append("-"+(str)(floor) +(str)(room) )
    

state = dict()

for i in LOG:
    x = i[1] + i[2]
    if(i[0] == '-'):
        state[x] = False
    else:
        state[x] = True

for i in state:
    if(state[i]):
        busy_cnts = busy_cnts+1
print( round(busy_cnts/max_rooms/max_floors*100), "%")