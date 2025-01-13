# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:26:05 2025

@author: Dino
"""


import random

name = ["A", "B", "C", "D"]

checkin = [10, 50, 60, 150]
checkout = [100, 70, 120, 300]

x1 = random.randint(10, 300)
x2 = random.randint(10, 300)
x3 = random.randint(10, 300)
x4 = random.randint(10, 300)
checkin = [x1, x2, x3, x4]
checkout = [x1 + random.randint(10, 150), 
            x2+ random.randint(10, 150),
            x3+ random.randint(10, 150),
            x4+ random.randint(10, 150)]



t_in = dict()
t_out = dict()
on_site = list()

for i in range(len(name)):
    t_in[checkin[i]] = name[i]
    t_out[checkout[i]] = name[i]



checkin.sort()
checkout.sort()

low = 0
high = 0
idx_max = len(checkin)-1
while(True):
    if(low <= idx_max):
        if(checkin[low] < checkout[high]):
            on_site.append(t_in[checkin[low]])
            print(checkin[low], on_site)
            low = low + 1
        elif(high<=idx_max):
            on_site.remove(t_out[checkout[high]])
            print(checkout[high], on_site)
            high = high + 1
    else:
        on_site = list()   
        print(checkout[high], on_site)
        break


        

