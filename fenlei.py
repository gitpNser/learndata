# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:32:22 2019
through study the "n-1" data to predict the [-1]

@author: pNser
"""
from sklearn import datasets
from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.)
digits = datasets.load_digits()
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1])
