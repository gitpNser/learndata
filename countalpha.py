# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:45:07 2019

@author: pNser

定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数
（允许输入大写字符，并且计数时不区分大小写）。
"""

def countchar(string):
    
    lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    count_alpha = [0] * 26
    
    string = string.lower()
    
    for i in range(26):
        count_alpha[i] = string.count(lst[i])
    
    return count_alpha
    
if __name__ == "__main__":
     string = input()
     print(countchar(string))