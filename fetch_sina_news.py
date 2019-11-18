# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:59:30 2019

@author: PNser copy Dazhuang@NJU
"""

import requests
import re
import jieba.posseg as pseg
from wordcloud import WordCloud
from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread

def fetch_sina_news():
    
    #pattern = re.compile('.shtml"target = "_blank">(.*?)</a><span>(.*?)</span></li>')
    
    Pattern = re.compile('"title":(.*?),')
    
    BASE_URL = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.4946381784772482&callback=jQuery111201072757076555062_1566453635049&_=1566453635051'
               
    with open('subjects.txt', 'w', encoding='utf-8') as f:
        try:
            r = requests.get(BASE_URL)
        except ConnectionError as err:
            print(err)
        
        data = r.text.encode('utf-8').decode('unicode-escape')
        
        p = re.findall(Pattern, data)
        
        for s in p:
            f.write(s)
            
def extract_words():
    
    with open('subjects.txt', 'r', encoding='utf-8') as f:
        news_subjects = f.readlines()
        
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
        content[item] = content.get(item,0) + 1
    
#    print(content)
# "Couldn't find space to draw. Either the Canvas size" 一直显示这个，不知道是不是因为背景是空白的原因，完全可以不用这个背景图  
#    d = path.dirname(__file__)
#    mask_image = imread(path.join(d,"mickey.png"))
#    
#    print(mask_image)
   
#    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey", mask=mask_image, max_words=10).generate_from_frequencies(content)
   
    
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey", max_words=10).generate_from_frequencies(content)

    
    # 显示词云图
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
    

if __name__ == "__main__":
    fetch_sina_news()
    extract_words()
    
    