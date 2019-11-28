# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:56:28 2019

@author: pNser
"""
import re
import requests
import pandas as pd

url = 'http://www.xbiquge.la/xiaoshuodaquan/'

try:
    
    r = requests.get(url)

except ConnectionError as err:
    
    print(err)
    
r.encoding = 'utf-8'

pattern = re.compile(r'<li><a href="(.*?)">(.*?)</a></li>')

novel = pd.DataFrame(re.findall(pattern,r.text))

novel.columns = ['URL','name']

novel.to_csv('biquge_all.csv',index=False)

novel2 = pd.read_csv('biquge_all.csv')

print(novel2)

#url1 = novel2[novel2['name']=='影视先锋']['URL'].values[0]
#print(url1)

book = input('pls input the name of the book:')

if book in novel2['name'].values:
    print(novel2[novel2['name']==book]['URL'].values[0])
else:
    print('NOT FOUND')    