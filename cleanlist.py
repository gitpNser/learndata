# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:37:50 2019

@author: pNser
"""

def clean_list(lst):
    
    new_list = []
    for item in lst:
        for c in item:
            if c.isalpha() != True:
                item = item.replace(c,'')
        new_list.append(item)
    
    return new_list

coffe_list = ['32Latte','_Americano30','/34Cappuccino','Mocha35']
cleaned_list = clean_list(coffe_list)

for k, v in zip(range(1,len(cleaned_list)+1),cleaned_list):
    print(k, v)
