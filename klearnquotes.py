# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 22:17:11 2019
根据涨跌数据规律进行聚类
20190806 result [2 1 1 2 2 1 1 0 1 2]
******** ****** [2 2 1 1 2 2 2 2 0 0]  before 20190528 
@author: pNser
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from yahooquotes import get_quotes_historical

def create_df(stock_code):
    quotes = get_quotes_historical(stock_code)
    list1 = ['close','date','high','low','open','volume']
    df_totalvolume = pd.DataFrame(quotes, columns=list1)
    df_totalvolume = df_totalvolume.fillna(df_totalvolume.mean())
    return df_totalvolume

listdji = ['MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'DD']

listTemp = [0] * len(listdji)
for i in range(len(listTemp)):
    listTemp[i] = create_df(listdji[i]).close
    
status = [0] * len(listdji)
for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
for i in range(len(status)):
    if len(status[i]) == 0:
        status.pop(i)
        break

kmeans = KMeans(n_clusters=3).fit(status)
pred = kmeans.predict(status)
print(pred)