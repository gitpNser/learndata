# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:53:17 2019

@author: pNser
"""
from sklearn import datasets
import pandas as pd
#import matplotlib.pyplot as plt
import statsmodels.api as sm

boston = datasets.load_boston()
X = pd.DataFrame(boston.data, columns = boston.feature_names)
y = pd.DataFrame(boston.target, columns = ['MEDV'])

X.drop('AGE', axis = 1, inplace = True)
X.drop('INDUS', axis = 1, inplace = True)
#X.drop('B', axis = 1, inplace = True)
#X.drop('ZN', axis = 1, inplace = True)
#X.drop('TAX', axis = 1, inplace = True)

X_add1 = sm.add_constant(X)

model = sm.OLS(y, X_add1).fit()

print(model.summary())
print(model.params)

##print(X.shape)
#plt.scatter(X['RM'],y,color='blue')
#plt.scatter(X['LSTAT'],y,color='blue')
 