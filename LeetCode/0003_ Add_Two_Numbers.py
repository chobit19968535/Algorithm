# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:30:16 2025

@author: Lycoris
"""

l1 = [2,4,3]
l2 = [5,6,4]

def inverse(a):
    l = len(a)
    
    if l%2 == 0:
        l = l/2
    else:
        l = (l-1)/2
        
    l = (int)(l)
    for i in range(l):
        tmp = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = tmp
    return a

    
class node(self):
    self.val = None
    self.next = None
    
    
    
    
inverse(l1)
inverse(l2)

a1 = str()
a2 = str()

for i in l1:
    a1 = a1 + str(i)
    
for i in l2:
    a2 = a2 + str(i)

a3 = str(int(a1) + int(a2))

l3 =list()
for i in a3:
    l3.append((int)(is