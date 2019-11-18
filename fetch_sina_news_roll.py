# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:59:30 2019

@author: PNser copy Dazhuang@NJU
"""

import requests
import re
import jieba.posseg as pseg
from wordcloud import WordCloud
#from os import path
import matplotlib.pyplot as plt
#from scipy.misc import imread
import time

def fetch_sina_news():
    
    #pattern = re.compile('.shtml"target = "_blank">(.*?)</a><span>(.*?)</span></li>')
    
    # 新闻标题在"title":之后,之前，所以比较好提取
    Pattern = re.compile('"title":(.*?),')
    
    # 因为是通过Jquery产生的页面，需要利用Chrome的检查工具里面Network来获取真正的地址，其中变化
    # 的点是page 和最后的数字（第一页用initial来记录），最后的数字按刷新来递增
    initial = 1566453635051
    
    #要抓取的页面数量
    MAX_page = 10
    
    #放置到subjects.txt文件中       
    with open('subjects.txt', 'w', encoding='utf-8') as f:
        for i in range(1,MAX_page+1):
            try:
                #拼接URL
                BASE_URL = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=%s&r=0.4946381784772482&callback=jQuery111201072757076555062_1566453635049&_=%s' % (str(i), str(initial -1 + i))
                r = requests.get(BASE_URL)
#                print(BASE_URL, r.status_code)
            except ConnectionError as err:
                print(err)
            
            # 因为网页的decode好像不是utf-8, 用unicode-escape来解码
            data = r.text.encode('utf-8').decode('unicode-escape')
            
            p = re.findall(Pattern, data)
            
            for s in p:
                f.write(s)
            
            #暂停5秒再抓取网页
            time.sleep(5)
            
def extract_words():
    
    #将文件内容抓取到news_subjects
    with open('subjects.txt', 'r', encoding='utf-8') as f:
        news_subjects = f.readlines()
    
    #设置停止词    
    stop_words = set(line.strip() for line in open('stopwords.txt',encoding='utf-8'))
    
    newsList = []
    
    for subject in news_subjects:
        if subject.isspace():
            continue
        
        #按行分词
        #n, nr, ns 都是名词的代表
        
        p = re.compile("n[a-z0-9]{0,2}")
        
        word_list = pseg.cut(subject)
        
        for word, flag in word_list:
            if not word in stop_words and p.search(flag) != None:
                newsList.append(word)
                
    content = {}
    
    for item in newsList:
        # 字典的get方法，get(key, default). 返回指定键的值，如果没有返回后面的默认值。不设置的话为None
        # 用在此处用来记录每个词的频率
        content[item] = content.get(item,0) + 1
    
#    print(content)
# "Couldn't find space to draw. Either the Canvas size" 一直显示这个，不知道是不是因为背景是空白的原因，完全可以不用这个背景图  
#    d = path.dirname(__file__)
#    mask_image = imread(path.join(d,"mickey.png"))
#    
#    print(mask_image)
   
#    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey", mask=mask_image, max_words=10).generate_from_frequencies(content)
   
    #比较容易理解了，字体，背景颜色，取最大词的个数，按词频生成词云图
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey", max_words=10).generate_from_frequencies(content)

    
    # 显示词云图
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
    

if __name__ == "__main__":
    fetch_sina_news()
    extract_words()
    
    