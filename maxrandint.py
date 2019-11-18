# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:38:53 2019

@author: pNser
"""
import random

i = 0

lst_randint = []

ranking = [0] * 101

while i < 500:
    lst_randint.append(random.randint(1,100))
    i +=1
    
lst_randint.sort()

for item in lst_randint:
    c = lst_randint.count(item)
    ranking[item] = c

for i in range(len(ranking)):
    if ranking[i] == max(ranking):
        print(i)
