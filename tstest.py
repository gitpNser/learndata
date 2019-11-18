# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:33:42 2019

@author: pNser reference to:Dazhang@NJU
"""

import tushare as ts
import numpy as np

#1 获取招商银行2018年下半年的数据，只保留前五列，按时间顺序排序
zsyh_hist_df = ts.get_hist_data('600036',start='2018-07-01',end='2018-12-31')
zsyh_hist_temp = zsyh_hist_df.iloc[:,0:5]
zsyh_hist_temp = zsyh_hist_temp.sort_index()

#2 输出最小交易量的一天以及交易量
min_day = zsyh_hist_temp.sort_values('volume').iloc[0,]
min_volume = min_day.volume
min_volume_date = min_day.name
max_day = zsyh_hist_temp.sort_values('volume').iloc[-1,]
max_volume = max_day.volume
max_volume_date = max_day.name
print('The lowest volume date is %s and the volume is %s' % (min_volume_date, min_volume))
print('The hisghest volume date is %s and the volume is %s' % (max_volume_date, max_volume))

#3 输出交易量大于1000000的记录
list_1000000 = zsyh_hist_temp[zsyh_hist_temp.volume > 1000000]
print(list_1000000)

#4 计算出收盘价大于开盘价的天数
list_up = zsyh_hist_temp[(zsyh_hist_temp.close > zsyh_hist_temp.open)]
print(len(list_up))

#5 计算前后两天开盘价的差异。一种方法计算差值，一种方法返回涨跌列表
#list_open_diff = []
#
#for i in range(len(zsyh_hist_temp)-1):
#    x = zsyh_hist_temp.iloc[i+1].open - zsyh_hist_temp.iloc[i].open
#    list_open_diff.append(x)   
#print(list_open_diff)
# 一个小函数就解决了以上问题并且是能带上日期的dataframe， 需要多多学习

print(zsyh_hist_temp.open.diff())

list_open_diff_new = np.sign(np.diff(zsyh_hist_temp.open))
print(list_open_diff_new)

#6 统计每月收盘价的平均值
month = [item[5:7] for item in zsyh_hist_temp.index]
print(zsyh_hist_temp.close.groupby(month).apply(np.mean))
    
