# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:05:55 2019

@author: pNser
"""
import re
import requests
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url,headers=None):
    
    try:
        r = requests.get(url, headers=headers)
    except ConnectionError as err:
        print(err)
        
    r.encoding = r.apparent_encoding
    
    #print(r.headers)
    
    return r.text

def getStockList(stockurl):
    
    lst = []
    
    html = getHTMLText(stockurl)
    soup = BeautifulSoup(html, 'lxml')
    
    a = soup.find_all('a')
    
    for item in a:
        try:
            href = item.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue
    
    #print(lst)
    return lst

def getStockinfo(lst,stockURL,fpath):
    
    for item in lst:
        
        #print(item)
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'}
        url = stockURL + item + '.html'
        html = getHTMLText(url,headers=headers)
        
#        print(url)
        print(html)
        break
        
        try:
            
            if html == '':
                continue
            
            infoDict = {}
            
            soup = BeautifulSoup(html, 'lxml')
            
            stockinfo = soup.find_all('div',attrs={'class':'stock-bets'})
            
            name = stockinfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            infoDict.uodate({'股票代码': item})
            
            keylist = stockinfo.find_all('dt')
            valuelist = stockinfo.find_all('dd')
            
            for i in range(len(keylist)):
                key = keylist[i].text
                value = valuelist[i].text
                infoDict[key] = value
                
            with open(fpth, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                print('writing %s' % (item))
                
        except:
            traceback.print_exc()
            continue
    

if __name__ == "__main__":
    
    stockurl = 'http://quote.eastmoney.com/stock_list.html'
    stockURL = 'https://gupiao.baidu.com/stock/'
    outputfile = 'c:/learndata/baidustock.txt'

    #slist = [] 
    
    slist = getStockList(stockurl)
    
    #print(slist)
    
    getStockinfo(slist, stockURL, outputfile)
    