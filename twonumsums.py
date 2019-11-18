# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:58:07 2019

@author: pNser

输入一个数字，在一个已知的不重复列表中查找是否有两数之和等于输入的数字，如有则返回
这两个数字的下标，要求其中一个数尽量小；如无则返回‘not found’
"""

def twonums_sum(n,lst):
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == n:
                return i,j
    return 'not found'



if __name__ == '__main__':
    
    n = eval(input())
    lst = [1,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65]
    
    print(twonums_sum(n,lst))
    

