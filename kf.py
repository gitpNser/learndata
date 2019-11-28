# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:40:52 2019

@author: pNser
"""

import tushare as ts
import numpy as np
import time

# 获取Kaifa的历史数据， 可以获取2.5年历史数据
kf = ts.get_hist_data('000021')

# 按日期排序
kf = kf.sort_index()
#
## 获取最高收盘价和最低收盘价的日期和价格
#min_day = kf.sort_values('close').iloc[0,]
#min_day_price = min_day.close
#min_day_date = min_day.name
#max_day = kf.sort_values('close').iloc[-1,]
#max_day_price = max_day.close
#max_day_date = max_day.name
#print('The lowest close day: %s & price: %s' % (min_day_date, min_day_price))
#print('The hihest close day: %s & price: %s' % (max_day_date, max_day_price))
#
## 输出交易量大于 500000的记录
#print(kf[kf.volume > 500000])
#
## 输出前后两天收盘价的差异
#print(kf.close.diff())
#print(np.sign(np.diff(kf.close)))
#
## 统计每年每月的收盘价平均值
#year_month = [item[0:7] for item in kf.index]
#print(kf.close.groupby(year_month).apply(np.mean))

breakup = kf[(kf.close > kf.ma5) & (kf.close > kf.ma10) & (kf.close > kf.ma20)]
breakdown = kf[(kf.close < kf.ma5) & (kf.close < kf.ma10) & (kf.close < kf.ma20)]


