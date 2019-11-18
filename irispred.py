# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:01:17 2019

@author: pNser copy Dazhuang@NJU
"""

from sklearn import cluster, datasets

iris = datasets.load_iris()

kmeans = cluster.KMeans(n_clusters = 3).fit(iris.data)

pred = kmeans.predict(iris.data)

for label in pred:
    print(label, end = '')  # 打印预测的标签
    
print('\n')

for label in iris.target:
    print(label, end='')    # 打印原始的标签

count = 0
for i in range(len(pred)):
    if pred[i] == iris.target[i]:
        count +=1

print(' The prediction correctness rate is: %.2f' % (count/len(pred)*100), end = '%')