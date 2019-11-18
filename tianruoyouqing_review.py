# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:48:26 2019

@author: pNser
"""
import requests
import re
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
from scipy.misc import imread
from wordcloud import WordCloud
import time

def get_comments_from_douban():
       
    step = 20
    
    for i in range(0,220,step):
        
        url = 'https://movie.douban.com/subject/1297710/comments?start=%s&limit=20&sort=new_score&status=P' % (str(i))
    
        headers = {    
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }
        
        try:
            
            r = requests.get(url,headers=headers)
            print(url)
            print(r.status_code)
            
        except ConnectionError as err:
            
            print(err)
        
        pattern = re.compile('<span class="short">(.*?)<\/span>')
        
        comments = re.findall(pattern,r.text)
        
        with open('comments.txt', 'a+', encoding='utf-8') as f:
            for c in comments:
                f.write(c)
        
        time.sleep(5)

def extract_words():
    
    with open('comments.txt', 'r', encoding='utf-8') as f:
        comments = f.readlines()
        
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    
    commentlist = []
    
    for comment in comments:
        if comment.isspace():
            continue
        
        #将词语分行
        #n, nr, ns, ...都是名词
        p = re.compile("n[a-z0-9]{0,2}")
        word_list = pseg.cut(comment)
        for word, flag in word_list:
            if not word in stop_words and p.search(flag) != None:
                commentlist.append(word)
    
    content = {}
    
    for item in commentlist:
        content[item] = content.get(item,0) + 1
        
    d = path.dirname(__file__)
    
    mask_image = imread(path.join(d, "micky.png"))
    
    wordcloud = WordCloud(font_path='simhei.ttf',background_color='grey',mask=mask_image,max_words=10).generate_from_frequencies(content)
    
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()


if __name__ == "__main__":
    
    get_comments_from_douban()
    extract_words()