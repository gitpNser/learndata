# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:31:37 2019

@author: pNser
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

boston = datasets.load_boston()

X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.DataFrame(boston.target,columns=['MEDV'])

X.drop('AGE', axis=1, inplace=True)
X.drop('INDUS', axis=1, inplace=True)

Xm = sm.add_constant(X)

model = sm.OLS(y, Xm).fit()

print(model.summary())