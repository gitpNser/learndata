# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:51:22 2019

@author: copied from dazhuang@NJU
"""
import math
def prime(x):
    
    if x==1:
        return False
    j = int(math.sqrt(x))
    for i in range(2,j+1):
        if x%i == 0:
            return False
    
    return True

def Gus(n):
    k=3
    while k < n:
        t = n-k
        if t < k:
            break
        if prime(t) and prime(k):
            return k, t
        k += 2

n = int(input('pls input a number:'))
if n > 4:
    a, b = Gus(n)
    print('{} = {} + {}'.format(n,a,b))
elif n == 4:
    print('{} = {} + {}'.format(4,2,2) )