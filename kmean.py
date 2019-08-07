# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:03:12 2019
search for good students base a known good student such as list9

@author: pNser
"""
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten

list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]
list7 = [79.0,96.0,100.0,65.0]
list8 = [87.0,99.0,95.0,99.0]
list9 = [100.0,99.0,95.0,98.0]

data = np.array([list1,list2,list3,list4,list5,list6,list7,list8,list9])
whiten = whiten(data)
centroids,_ = kmeans(whiten,3)  #can seperate into 2 groups also
result,_ = vq(whiten,centroids)
print(result) 
