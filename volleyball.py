# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:21:37 2019

@author: pNser
"""
import re
import requests

url = 'http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'

try:
    
    r = requests.get(url)
    
except ConnectionError as err:
    
    print(err)


pattern = re.compile('href=.*?>(.*?)<\/a>.*?\s+.*?\s+<\/td>\s+<td>(.*?)<\/td>\s+<td.*?bold">(.*?)<\/td>\s+<td.*?rightborder">(.*?)<\/td>')

team = re.findall(pattern, r.text)

print(team)
