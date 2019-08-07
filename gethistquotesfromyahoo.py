# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:36:51 2019

@author: pNser
"""
import requests, re, json
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

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

def create_quotes_df(stock_code):
    
    quotes = get_quotes_historical(stock_code)
    list1 = []
    list2 = []
    for i in range(len(quotes)):
        x = date.fromtimestamp(quotes[i]['date'])
        y = date.strftime(x, '%Y-%m-%d')
        list1.append(y)
        list2.append(y[0:7])
    
    quotes_df = pd.DataFrame(quotes, index = list1)
    quotes_df = quotes_df.drop(['date'], axis = 1)
    quotes_df['month'] = list2
    
    return quotes_df

# 暂时屏蔽，配合老师的模式，方便修改图形属性
#def plot_close_mean(stock_code):
#    
#    quotes_df = create_quotes_df(stock_code)
#    
#    close_mean = quotes_df.groupby('month').close.mean()
#    
#    x = close_mean.index
#    y = close_mean.values
#    
#    return plt.plot(x,y)
#
#plot_close_mean('KO')

def close_mean(stock_code):
    
    quotes_df = create_quotes_df(stock_code)
    
    close_mean = quotes_df.groupby('month').close.mean()
    
    return close_mean

x_KO = close_mean('KO').index
y_KO = close_mean('KO').values

x_IBM = close_mean('IBM').index
y_IBM = close_mean('IBM').values

plt.subplot(211)
plt.plot(x_KO,y_KO,color='r',marker='o')
plt.subplot(212)
plt.plot(x_IBM,y_IBM,color='green',marker='o')
    

