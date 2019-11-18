# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:39:11 2019

@author: pNser
"""
import math

def prime(x):
    
    if x == 1:
        return False
    
    n = int(math.sqrt(x))
    
    for i in range(2,n+1):
        if x%i == 0:
            return False
    
    return True

def monisen(no):
    
    i = 0
    j = 2
    m = []
    
    while i < no:
        p = math.pow(2,j) - 1
        if prime(j) and prime(p):
            i += 1
            m.append(p)
        j +=1
    
    return int(m[-1])

print(monisen(int(input())))