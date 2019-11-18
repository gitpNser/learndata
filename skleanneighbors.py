# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:52:10 2019

@author: pNser copy Dazhuang@NJU
"""

from sklearn import neighbors, datasets, svm

iris = datasets.load_iris()
# 利用K Neareast Neighbors 算法
knn = neighbors.KNeighborsClassifier()
# 从已有数据学习
knn.fit(iris.data, iris.target)
# 利用分类模型机型未知数据的预测（确定标签）
print(knn.predict([[5.0, 3.0, 5.0, 2.0]]))

svc = svm.LinearSVC()

svc.fit(iris.data, iris.target)   # 学习

print(svc.predict([[5.0, 3.0, 5.0, 2.0]]))

