# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:44:16 2019

@author: pNser
"""
import re
import requests

def getHTMLText(url):
    
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)
        
    r.encoding = r.apparent_encoding
    
    return r.text

if __name__ == "__main__":
    
    url = 'https://search.jd.com/Search?keyword=%s' % (input('pls input keyword:'))
    html = getHTMLText(url)
    print(html)
