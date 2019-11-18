# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:11:30 2019

@author: pNser copy:  北京理工大学MOOC
"""
import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)
        
    r.encoding = r.apparent_encoding
    
    return r.text

def fillUlist(ulist, html):
    
    soup = BeautifulSoup(html, 'lxml')
    
    # 整个排名信息封装在tbody标签内
    # 每个学校的所有信息都封装在 tr标签内
    # 每个学校具体的每个信息又封装在td标签内
    # 遍历tbody 标签下所有的tr标签，然后将每个tr标签内的td标签字符串传递给newlist
    # 然后将newlist传递给ulist。
    # 相对于直接使用所有td信息直接传递给ulist ,这样就可以不用每14个td整理一次来做大学信息合并
    for tr in soup.find('tbody').children:
        # 确定tr是bs4的标签才进行下一步遍历
        # 剔除掉非标签的tr字符串干扰
        if isinstance(tr, bs4.element.Tag):
            newList = []
            for td in tr('td'):
                newList.append(td.string)
            ulist.append(newList)
            
def printulist(ulist,num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    # chr(12288)是中文空格符
    # 在信息宽度不够需要字符填充时使用中文空格填充而不是西文空格填充，避免对齐问题
    print(tplt.format('排名','学校','省市',chr(12288)))
    # 输出对应数字的大学信息
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    
if __name__ == "__main__":
    
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUlist(uinfo, html)
    printulist(uinfo,20)