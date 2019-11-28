# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:12:11 2019

@author: pNser
"""
import re
import requests
from bs4 import BeautifulSoup
import traceback
import time

def getHTMLText(url):
    
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    
    try:
        r = requests.get(url, headers=headers, timeout=30)
        print(r.status_code)
    except ConnectionError as err:
        print(err)
        
    r.encoding = r.apparent_encoding
    
#    print(r.text)
    
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
            #laohu8.com只需数字代码就可查询具体股票数据
        except:
            continue
    
    #print(lst)
    return lst

def getStockinfo(lst,stockURL,fpath):
    
    for item in lst:
        
        #print(item)
        url = stockURL + item[2:]
        html = getHTMLText(url)
        print(url)
#        print(html)
#        break
        
        try:
            
            if html == '':
                continue
            
            infoDict = {}
            
            soup = BeautifulSoup(html, 'lxml')
            
            stockinfo = soup.find('div',attrs={'class':'detail-data'})

#            print(stockinfo)
#            break

            keylist = stockinfo.find_all('dt')
            valuelist = stockinfo.find_all('dd')
#            print(keylist,valuelist)
#           
            key = []
            val = []
            
            for td in keylist:
                key.append(td.string)
            
            for dd in valuelist:
                val.append(dd.string)
            
#            print(key,val)
                
#            break
            
 
            for i in range(len(key)):
                infoDict[key[i]] = val[i]
#                
#            print(infoDict)
#            break
                           
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(item)
                f.write('\n')
                f.write(str(infoDict) + '\n')
                print('writing %s' % (item))
           
            
        except:
            time.sleep(3)
            traceback.print_exc()
            continue
    

if __name__ == "__main__":
    
    stockurl = 'http://quote.eastmoney.com/stock_list.html'
    stockURL = 'https://www.laohu8.com/stock/'
    outputfile = 'c://learndata//laohu8.txt'

    #slist = [] 
    
    slist = getStockList(stockurl)
    
    
#    print(slist)
    
    
    
    getStockinfo(slist, stockURL, outputfile)
    