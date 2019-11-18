# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:32:41 2019

@author: pNser

对于一个已分词的句子（可方便地扩展到统计文件中的词频）：
我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！
可以用collections模块中的Counter()函数方便地统计词频，例如可用如下代码：
import collections
import copy
s = "我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！/"
s_list = s.split('/') 
# 为避免迭代时修改迭代对象本身，创建一个列表的深拷贝，也可用浅拷贝s_list_backup = s_list[:]
s_list_backup = s_list[:]
[s_list.remove(item) for item in s_list_backup if item in '，。！”“']
collections.Counter(s_list)
这个问题也可以通过字典来解决，请编写用字典解决本问题的程序，为便于OJ系统自动判断，程序最后输出某个单词的词频。

"""

def countfeq(s):
   
   dict = {}
   
   s = s.split()
   
   for item in s:
       
       if item[-1] in ',.':
           item = item[:-1]
           dict[item] = dict.get(item,0) + 1
       else:
           dict[item] = dict.get(item,0) + 1
        
    
   return dict
    
if __name__ == "__main__":
   s = "Not clumsy person in this world, only lazy people, only people can not hold out until the last."
   s_dict = countfeq(s.lower())
   word = input()
   
   if word in s_dict:
       print(s_dict[word])
   else:
       print('0')
    
   
   # 基于s_dict判断word的词频并输出（可能是0次）