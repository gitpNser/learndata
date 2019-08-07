# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:33:04 2019

@author: pNser
"""
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd

iris = datasets.load_iris()


list1 = [0] * len(iris.data)
for i in range(50):
    list1[i] = iris.target_names[0]
for i in range(50,100):
    list1[i] = iris.target_names[1]
for i in range(100,150):
    list1[i] = iris.target_names[2]

# 在已知名字分布的情况下可以
# list1 = ['setosa'] * 50 + ['versicolor'] * 50 + ['verginia'] * 50

#list2 = []
#for item in iris.feature_names:
#    item = item[0:10].replace(' ','')

# 已知属性的情况下也不用上面那么复杂，并且还需要使用replace去除空格，得到的属性名还不可知
list2 = ['sepalL','sepalW','petalL','petalW']
    
iris_df = pd.DataFrame(iris.data, index = list1)
iris_df.columns = list2

plt.title('Iris plot')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
x1 = iris_df[iris_df.index == 'setosa'].sepalL
y1 = iris_df[iris_df.index == 'setosa'].petalL
x2 = iris_df[iris_df.index == 'versicolor'].sepalL
y2 = iris_df[iris_df.index == 'versicolor'].petalL
x3 = iris_df[iris_df.index == 'virginica'].sepalL
y3 = iris_df[iris_df.index == 'virginica'].petalL

#获取以上数据还有更简单的方法
# x = [item[0] for item in iris.data] #直接提取第一列数据
# y = [item[2] for item in iris.data] #直接提取第三列数据
#然后直接分别截取50项数据 x[:50],x[50,100],x[100:]
#将名称直接交给label来备注
#以上就不需要将iris.data转换成为dataframe并增加index 和columns

#题目需要使用散点图
#plt.plot(x1,y1,'ro',label='setosa')
#plt.plot(x2,y2,'g*',label='versicolor')
#plt.plot(x3,y3,'bD',label='virginical')
#plt.legend(loc='best')

plt.scatter(x1,y1,color='red',marker='o',label='setosa')
plt.scatter(x2,y2,color='green',marker='*',label='versicolor')
plt.scatter(x3,y3,color='blue',marker='D',label='virginical')
plt.legend(loc='best')