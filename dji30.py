# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:07:18 2019

@author: pNser
"""
import requests
import re

def get_data():
    
    try:
        r = requests.get('https://money.cnn.com/data/dow30/')
    except ConnectionError as err:
        print(err)
    
    pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\s+.*?class="wsod_stream">(.*?)<\/span>')
    
    dji_list_in_text = re.findall(pattern, r.text)
    
    return dji_list_in_text


dji_list = get_data()

print(dji_list)

    
