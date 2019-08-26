# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:09:35 2019

@author: pNser
"""

import requests
from bs4 import BeautifulSoup

URL = 'http://www.xbiquge.la/3/3322/19176354.html'

r = requests.get(URL)

r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')

content = soup.find("div",{"id":"content"}).get_text()

print(content)

with open('biquge.txt', 'a+', encoding='utf-8') as f:
    f.write(content)