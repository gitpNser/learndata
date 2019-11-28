# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:51:35 2019

@author: pNser
"""
import requests
#import re
import pandas as pd
from bs4 import BeautifulSoup
#import numpy as np

def getHTMLText(URL):
    
    try:
        r = requests.get(URL)
    except ConnectionError as err:
        print(err)
    
    r.encoding = 'utf-8'
    
    text = r.text
    
    return text
        
def fillUnivList(text):
   
    UnivList = []
    
    soup = BeautifulSoup(text, 'lxml')
    
    for item in soup.find_all('td'):
        UnivList.append(item.string)    

    newList = []
    
    for i in range(0,len(UnivList),14):
        newList.append(UnivList[i:i+14])
    
    columns = ['排名','名称','省市','总分','生源质量','培养结果','社会声誉','科研规模','科研质量','顶尖成果','顶尖人才','科技服务','成果转化','学生国际化']
    
    UnivRanking = pd.DataFrame(newList)
    
    index = range(1, len(UnivRanking)+1)
    
    UnivRanking.index = index
    UnivRanking.columns = columns

    return UnivRanking
        

if __name__ == "__main__":
    
    URL = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    text = getHTMLText(URL)
    print(fillUnivList(text).iloc[:20,:4])
#    fillUnivList(text)