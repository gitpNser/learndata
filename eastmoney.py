# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:12:11 2019

@author: pNser
"""
import re
import requests
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url):
    
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)
        
    r.encoding = r.apparent_encoding
    
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
        url = stockURL + item + '.html'
        html = getHTMLText(url)
#        print(html)
#        break
        
        try:
            
            if html == '':
                continue
            
            infoDict = {}
            
            soup = BeautifulSoup(html, 'lxml')
            
            stockinfo = soup.find('div',attrs={'class':'qphox layout mb7'})
#            print(stockinfo)
#            break
            
#            price = stockinfo.find_all('strong',attrs={'class':'xp1'})[0]
#            price = stockinfo.find_all(id='price9')[0].string
#            print(price)
#            break
#            infoDict.update({'股票价格':price.text.split()[0]})
#            infoDict.uodate({'股票代码': item})
            
#            keylist = stockinfo.find_all('tr')
#            print(keylist)
#            break
            valuelist = stockinfo.find_all('td')
            print(valuelist)
            
            key = []
            val = []
            for i in range(0,len(valuelist)-1,2):
                key.append(valuelist[i].text)
                val.append(valuelist[i+1].text)
                
            print(key, val)   
            for i in range(len(key)):
                infoDict[key[i]] = val[i]
                
            print(infoDict)
            break
            
#            for i in range(len(keylist)):
#                key = keylist[i].text
#                value = valuelist[i].text
#                infoDict[key] = value
                
            with open(fpth, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                print('writing %s' % (item))
                
        except:
            traceback.print_exc()
            continue
    

if __name__ == "__main__":
    
    stockurl = 'http://quote.eastmoney.com/stock_list.html'
    stockURL = 'http://quote.eastmoney.com/'
    outputfile = 'c:/learndata/eastmoney.txt'

    #slist = [] 
    
    slist = getStockList(stockurl)
    
    #print(slist)
    
    getStockinfo(slist, stockURL, outputfile)
    