# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:09:35 2019

@author: pNser
"""

import requests
from bs4 import BeautifulSoup

URL = 'http://www.xbiquge.la/10/10489/4535761.html'

r = requests.get(URL)

r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')



#content = soup.find("div",{"id":"content"}).get_text()

#
#
#content = ''
#for child in soup.div.attrs[content].children:
#    content += child.string
                

#print(content)
#
#with open('biquge.txt', 'a+', encoding='utf-8') as f:
#    f.write(content)