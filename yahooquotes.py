# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:39:01 2019

@author: pNser copy Dazhuang@NJU
"""
import requests, re, json
import pandas as pd
from datetime import date

def get_quotes_historical(stock_code):
    
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)
    
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
        
    return [item for item in quotes if not 'type' in item]

quotes = get_quotes_historical('AXP')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x, '%Y-%m-%d')
    list1.append(y)
    
quotesdf_ori = pd.DataFrame(quotes, index = list1)
quotesdf = quotesdf_ori.drop(['date'], axis = 1)
print(quotesdf)