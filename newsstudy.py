# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:45:41 2019

@author: pNser
"""
import requests
import re
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
from scipy.misc import imread
from wordcloud import WordCloud
#import time

def get_roll_news_from_sina(url):
    
#    headers = {
#        'Referer': 'https://news.sina.com.cn/roll/'
##        'Sec-Fetch-Mode': 'no-cors'
#        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'
#    }
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)
        
    pattern = re.compile('"title":"(.*?)"')
    
    data = r.text.encode('utf-8').decode('unicode-escape')
    
    titles = re.findall(pattern, data)
    
    with open('titles.txt', 'w', encoding='utf-8') as f:
        for s in titles:
            f.write(s)


def extract_words():
    
    with open('titles.txt', 'r', encoding='utf-8') as f:
        news_titles = f.readlines()
        
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    
    newslist = []
    
    for title in news_titles:
        if title.isspace():
            continue
        
        #将词语分行
        #n, nr, ns, ...都是名词
        p = re.compile("n[a-z0-9]{0,2}")
        word_list = pseg.cut(title)
        for word, flag in word_list:
            if not word in stop_words and p.search(flag) != None:
                newslist.append(word)
    
    content = {}
    
    for item in newslist:
        content[item] = content.get(item,0) + 1
        
    d = path.dirname(__file__)
    
    mask_image = imread(path.join(d, "micky.png"))
    
    wordcloud = WordCloud(font_path='simhei.ttf',background_color='grey',mask=mask_image,max_words=10).generate_from_frequencies(content)
    
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()

if __name__ == "__main__":

    url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.3694237552312014&callback=jQuery111203729764560510138_1565873600031&_=1565873600033'
    get_roll_news_from_sina(url)
    extract_words()    