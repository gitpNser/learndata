# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:45:19 2019

@author: pNser
"""
def hanoi(a,b,c,n):
    if n==1:
        print(a, '->', c)
    else:
        hanoi(a,c,b,n-1)
        print(a, '->', c)
        hanoi(b,a,c,n-1)
        
hanoi('a','b','c',4)
