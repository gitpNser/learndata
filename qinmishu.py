# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:47:03 2019

@author: pNser
"""
def fac(x):
    
    s = 0
    n = int(x/2)
    for i in range(1,n+1):
        if x%i==0:
            s +=i
    
    return s

n = int(input())

#for i in range(1,n):
#    for j in range(i+1,n):
#        if fac(i) == j and fac(j)==i:
#            print('{}-{}'.format(j,i))

for i in range(n):
    if fac(fac(i))==i and i<fac(i):
        print('{}-{}'.format(i,fac(i)))