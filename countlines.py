# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:17:13 2019

@author: pNser
"""
import os

def countlines(fname):
    

    with open(fname, encoding='utf-8') as f:
        cNames = f.readlines()
    
    count = len(cNames)
 
    
    print('%s has %d lines.' % (fname, count))

path = 'd://work'

for fname in os.listdir(path):
    if fname.endswith('.txt'):
        print(fname)
        countlines(fname)
