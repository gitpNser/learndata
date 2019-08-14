# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:59:33 2019

@author: pNser
"""

import pandas as pd

stu = pd.read_excel('stu.xlsx')

list_sum = []

for i in range(len(stu)):
    c = stu['Python'][i]+stu['Math'][i]
    list_sum.append(c)    
stu['Sum'] = list_sum

# 更简单的方法，真是只有想不到，没有做不到啊
#stu['sum'] = stu['Python'] + stu['Math']

stu.to_excel('stu.xlsx')
