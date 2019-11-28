# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:37:45 2019

@author: pNser
"""
n = int(input('pls input a int:'))

result = []

j = 0

for i in range(1,101):
    
    if i%n != 0 and (i-n)%10 != 0 and i//10 != n:
        
        result.append(i)
        
        i +=1
    
for i in range(0,len(result),10):
    
    print(result[i:i+10])
    
