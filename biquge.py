# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:09:17 2019

@author: pNser
"""
import requests
import re
#import os
import pandas as pd
from bs4 import BeautifulSoup
#import chardet

def get_charpters(book,bookurl):
    
    BASE_URL = 'http://www.xbiquge.la'
    book_URL = bookurl
    
    try:
        r = requests.get(book_URL,timeout=30)
    except ConnectionError as err:
        print(err)
        
    # requests 库自身编码为“ISO-8858-1”，有时不能准确推测出网页编码就会导致中文显示乱码
    # 利用encoding属性将编码修改为"utf-8"
    r.encoding = 'utf-8'
        
    pattern = re.compile("<dd><a href=(.*?)>(.*?)</a></dd>")
    
    charpter_info = re.findall(pattern, r.text)    

    charpter_info_df = pd.DataFrame(charpter_info)
    
    charpter_info_df.columns = ['URL', 'C_Names']
    
    for i in range(len(charpter_info_df)):
        charpter_info_df['URL'][i] = BASE_URL + charpter_info_df['URL'][i][1:-2]


#def get_content(url):
    
    book_name = book + '.txt'
    
    with open(book_name, 'a+', encoding='utf-8') as f:
        
        f.seek(0)
        data = f.read()
#        print(data)
##        f.seek(1)

# 要读取数据需使用values，直接读取dataframe只是读取表头 
# 读取第一列不能用column值，要用序列0,1,2等。 此处存疑？
        for item in charpter_info_df.values:
            if item[0] in data:
                continue
            else:
                try:
                    r_content = requests.get(item[0],timeout=10)
                    print('Downloing Charpter: %s' % (item[1]))
                except ConnectionError as err:
                    print(err)
                            
                r_content.encoding = 'utf-8'

                soup = BeautifulSoup(r_content.text, 'lxml')      
                
                content = soup.find("div",{"id":"content"}).get_text()
                
                f.write(item[0])
                f.write('\n')
                f.write(item[1])
                f.write('\n')
                f.write(content)
                f.write('\n')
    
                
#    return charpter_info_df


    
if __name__ == "__main__":
    
    book = input('请输入想下载的书籍：')
    
    novel = pd.read_csv('biquge_all.csv')
    
    if book in novel['name'].values:
        bookurl = novel[novel['name']==book]['URL'].values[0]
        get_charpters(book,bookurl)
    else:
        print('NOT FOUND')
    

        

    
    
