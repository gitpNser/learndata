# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:27:35 2019

@author: pNser
"""
import pandas as pd

scores = pd.read_excel('scores.xlsx')

scores.boxplot()
