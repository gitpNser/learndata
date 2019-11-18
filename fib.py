# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:34:34 2019

@author: pNser
"""
def fib1(n):
    a,b = 0,1
    count = 1
    while count < n:
        a,b = b,a+b
        count +=1
    
    print(a)
    
def fib2(n):
    if n==1 or n==2:
        return n-1
    else:
        return fib2(n-1)+fib2(n-2)
    
fib1(10)
print(fib2(10))
