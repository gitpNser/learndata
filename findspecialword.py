# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:01:48 2019

@author: pNser
"""
slist = ['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']

for item in slist:
    item_tmp = item.lower()
    for ch in item_tmp:
#        print(ch)
        if ch in 'aeiou' or ch in '0123456789':
            break
    else:
        print(item)
