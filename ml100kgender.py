# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:08:13 2019

@author: pNser copy Dazhuang@NJU
"""
import numpy as np
import pandas as pd

#  读入数据
unames = ['user id','age','gender','occupation','zip code']
users = pd.read_table(r'ml-100k\u.user', sep='\|', names = unames, engine='python', encoding='utf-8')
rnames = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_table(r'ml-100k\u.data', sep='\t', names = rnames, engine='python', encoding='utf-8')

# 选择需要的数据列，提高效率
user_df = pd.DataFrame()
user_df['user id'] = users['user id']
user_df['gender'] = users['gender']

rating_df = pd.DataFrame()
rating_df['user id'] = ratings['user id']
rating_df['rating'] = ratings['rating']

# 将数据合并
rating_df = pd.merge(user_df, rating_df)

# 利用pandas 中的数据透视表pivot_table()函数对数据进行聚合，  
gender_table = pd.pivot_table(rating_df, index = ['gender', 'user id'], values = 'rating')

gender_df = pd.DataFrame(gender_table)

# 按性别分开

Female_df = gender_df.query("gender == ['F']")
Male_df = gender_df.query("gender == ['M']")

# 计算标准差

Female_std = np.std(Female_df)
Male_std = np.std(Male_df)

print('Gender' '\nF\t%.6f' % Female_std, '\nM\t%.6f' % Male_std)
#Gender
#F       0.480358 
#M       0.429755
