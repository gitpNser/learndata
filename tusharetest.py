# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:50:23 2019

@author: pNser

利用
Tushare 包中的 接口函数 获取 招商银行（股票代码 600036 201 9 年 第一季度 的股票
数据并完成如下数据处理和分析任务：
1.数据只保留 date 、 open 、 high 、 close 、 low 和 volume 这几个属性，并按时间先后顺序对
数据进行排序；
2.选择 2019 年一季度和 1 月该股票最高价 high 和最低价 low 数据。
3.输出这一季度内成交量最低和最高那两天的日期和分别的成交量；
4.列出成交量在列出成交量在100000以上的记录；
5.计算这一季度中收盘价(clsoe)高于开盘价（open）的天数；
6.计算前后两天开盘价的涨跌情况，用两种方式表示，第一种输出每两天之间的差值
（后一天减去前一天），第二种输出一个开盘价涨跌列表，涨用1表示，跌用-1表示[提示：可使用diff()方法和sign()函数]
7.绘制绘制2019年年1月该股票最高价月该股票最高价high和最低价low的折线图；
8.绘制该股票在此季度内每日收盘价与开盘价之差与当日成交量之间的散点图。。
"""

import tushare as ts
import numpy as np
import matplotlib.pyplot as plt

# 使用tushare端口获取股票历史信息，包含'open', 'high', 'close', 'low', 'volume', 
#'price_change', 'p_change','ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20']
df = ts.get_hist_data('600036',start='2019-01-01',end='2019-03-31')

# 通过切片保留前五项
df = df.iloc[:,:5]

# 按index排序，默认index就是股票交易日期
df.sort_index(inplace=True)

# 输出一季度'high','low'
#print(df.loc[:,['high','low']])

# 输出一月份'high','low'
#print(df.loc['2019-01-01':'2019-01-31',['high','low']])

# 输出这一季度内成交量最低和最高那两天的日期和分别的成交量
#max_Day = df[df.volume==df.volume.max()].iloc[0,:].name
#max_Volume = df[df.volume==df.volume.max()].iloc[0,:].volume
#min_Day = df[df.volume==df.volume.min()].iloc[0,:].name
#min_Volume = df[df.volume==df.volume.min()].iloc[0,:].volume
#print("the min volume of {} is at {}".format(min_Volume, min_Day))
#print("the max volume of {} is at {}".format(max_Volume, max_Day))

# 输出成交量大于100000的记录
#print(df[df.volume>100000])

#计算这一季度中收盘价(clsoe)高于开盘价（open）的天数
#print(len(df[df.close>df.open]))

#6.计算前后两天开盘价的涨跌情况，用两种方式表示，第一种输出每两天之间的差值
#print(df.open.diff())

#第二种输出一个开盘价涨跌列表，涨用1表示，跌用-1表示[提示：可使用diff()方法和sign()函数]
#print(np.sign(np.diff(df.open)))

#绘制2019年年1月该股票最高价月该股票最高价high和最低价low的折线图
df_jan= df.loc["2019-01-01":'2019-01-31',['high','low']]
df_jan.sort_index().plot()

#绘制该股票在此季度内每日收盘价与开盘价之差与当日成交量之间的散点图
#plt.scatter(df.close-df.open,df.volume)