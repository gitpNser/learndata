# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:46:22 2019

@author: pNser
"""
for i in range(1,1001):
    s=0
    
    for j in range(1,i):
        if i%j == 0:
            s +=j
    
    if s == i:
        print('\n',i,'',end='')
        print('The factors are:', end='')
        
        for j in range(1,i):
            if s%j == 0:
                print(j, end=' ')
        
        

