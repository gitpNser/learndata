# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:22:11 2019

@author: pNser
"""
import seaborn as sns

titanic_df = sns.load_dataset('titanic')

titanic_df.isnull()

print(titanic_df)
