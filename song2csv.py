# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:11:15 2019

@author: pNser
"""

import pandas as pd
import re

list1 = ['The rolling Stone','Beatles','Guns N Roses','Metallica']
list2 = ['Satisfication','Let it be','Dont cry','Nothing else matter']
df_song = pd.DataFrame()
df_song['singer'] = list1
df_song['song'] = list2
print(df_song)
df_song.to_csv('song.csv')

#with open(r'c:\learndata\song.csv' ) as f:
#    lines = f.readlines()
#    pattern = '.*?\,(.*?)\\n'
#    list1 = []
#    for item in lines[1:]:
#        print(item)
#        c = re.findall(pattern, item)
#        list1.append(c)
#    print(list1)

result = pd.read_csv('song.csv')
print(result['song'])