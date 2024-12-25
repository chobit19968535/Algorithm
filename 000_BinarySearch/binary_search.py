# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:36:04 2024

@author: Lycoris
"""
import random
import math

cnt = 10
lb = 0
up = 50
result  = -1

data = [random.randint(lb, up) for _ in range(cnt)]
data.sort()

X = random.randint(lb, up)



# Main
def BinarySearch_Modify(X):
    low = 0
    high = len(data) - 1
    
    
    while(low < high):
        mid = math.floor( (low + high)/2)
        if data[low] > X or data[high] < X:
            return -1
        
        if data[low] == X:
                return low
        elif data[high] == X:
                return high
            
        else:
            if data[mid] == X:
                return mid
            elif data[mid] > X:
                high = mid-1
                low = low+1
                
            elif data[mid] < X:
                low = mid+1
                high = high -1
    return -1

def BinearySearch_Normal(X):
     low = 0
     high = len(data)
     
     while(low<high):
         mid = math.floor( (low+high)/2 )
         
         if data[mid] == X:
            return mid
        
         elif data[mid] > X:
            high = mid - 1
         elif data[mid] < X:
            low = mid+1          
     return -1
             

def main():
    # return BinarySearch_Modify(X)
    return BinearySearch_Normal(X)
     
result = main()
