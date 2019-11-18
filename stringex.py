# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:04:29 2019

@author: pNser
"""

def reverse_string(str):
    
    new_str = str.split(' ')
    new_str = new_str[::-1]
    reverse_str = ' '.join(new_str)
    print(reverse_str)
    
    
def move_substr(s,flag,n):
    
    if n > len(s):
        return -1
    else:
        if flag == 1:
            return s[n:]+s[:n]
        if flag == 2:
            return s[-n:]+s[:-n]





#string = input('input a string:')
#reverse_string(string)
            
s = input('pls innput a string:')
flag = int(input('pls input the direction.1 for left and 2 for right:'))
n = int(input('pls input the steps need to move:'))
str = move_substr(s,flag,n)
print(str)