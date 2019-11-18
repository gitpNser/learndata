# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:05:06 2019

@author: pNser
"""
import re
from bs4 import BeautifulSoup
import requests

url = 'https://book.douban.com/subject/1084336/comments/'

try:
    
    r = requests.get(url)

except ConnectionError as err:
    
    print(err)
    
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')

# soup 获取内容只要按tag，及 attr 顺序列出即可
comments = soup.find_all('span','short')

for item in comments:
    print(item.string)

s = 0

pattern1 = re.compile('<a href="https://www.douban.com/people/(.*?)/">(.*?)</a>')
pattern2 = re.compile('<span class="user-stars allstar(.*?) rating"')

stars = re.findall(pattern2, r.text)

for star in stars:
    s += int(star)
    
print(s)

comment_infos = re.findall(pattern1, r.text)

for item in comment_infos:
    print(item)
