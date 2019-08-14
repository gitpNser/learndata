# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:18:29 2019

@author: pNser
"""
from nltk.corpus import gutenberg, inaugural
from nltk.probability import *

## 导出hamlet这本小说所有的单词
#allwords = gutenberg.words('shakespeare-hamlet.txt')
#
#
#print(len(allwords))
#
## 其中Hamlet出现的次数
#print(allwords.count('Hamlet'))
#
#A = set(allwords)
#
##找出单词长度大于12 的单词
#longwords = [w for w in allwords if len(w) > 12]
#
#print(sorted(longwords))
#
## 挖掘Hamlet这本小说中前20各最够词频的单词
#fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])
#print(fd2.B())
#print(fd2.N())
#fd2.tabulate(20)
#fd2.plot(20)
#fd2.plot(20, cumulative=True)

fd3 = FreqDist([s for s in inaugural.words()])
print(fd3.freq('freedom'))

cfd = ConditionalFreqDist((fileid, len(w)) for fileid in inaugural.fileids() for w in inaugural.words(fileid) if fileid > '1980' and fileid < '2010')
print(cfd.items())
cfd.plot()