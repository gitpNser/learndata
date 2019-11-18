# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:16:56 2019

@author: pNser
"""
with open('article.txt','r') as f:
    data = f.read()
    
words = data.split()

list_w = []

for word in words:
    if word[-3:] == '...':
        word = word[:-3]
        list_w.append(word)
    if word[-1] in ',.?!':
        word = word[:-1]
    list_w.append(word)
    
result = sorted(list_w, key=len, reverse=True)

maxlen= len(result[0])

for word in set(list_w):
    n = len(word)
    if n == maxlen:
        print(word)

