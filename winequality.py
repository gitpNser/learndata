# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:48:21 2019

@author: pNser copy Dazhuang@NJU
"""
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import warnings

warnings.filterwarnings('ignore')

try:
    wine = pd.read_csv('winequality-red.csv', sep=';')
except:
    print('Can not find the file.')
    