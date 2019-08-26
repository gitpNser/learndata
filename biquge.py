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

def get_charpters(id_1,id_2):
    
    BASE_URL = 'http://www.xbiquge.la'
    book_URL = 'http://www.xbiquge.la/%s/%s' % (id_1, id_2)
    
    try:
        r = requests.get(book_URL)
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
    
    URL_list = str(id1) + str(id2) + 'list' + '.txt'
    
    with open(URL_list, 'a+', encoding='utf-8') as f:
        
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
                    r_content = requests.get(item[0])
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
    id1 = 19
    id2 = 19620
    get_charpters(id1,id2)

    
    
