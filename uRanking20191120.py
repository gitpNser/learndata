# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:43:22 2019

@author: pNser
"""
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print('链接错误')
    return r.text

def fillUnivList(ulist,html):
    
    soup = BeautifulSoup(html,'lxml')
    
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUlist(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","分数"))
    
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
    

if __name__ == '__main__':
    
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUlist(uinfo,20)