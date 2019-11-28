# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:59:52 2019

@author: copy dazhuang@NJU
"""

def proc(n):
    if n < 0:
        print('-', end = ' ')
        n = -n
    if n // 10:
        proc(n // 10 )
    print(n % 10, end = '  ')
     
proc(-345)

# 递归的思想就是先往下递归，返回的时候从最底层开始返回
# 所以虽然一开始得出的345，但是345%10是最后返回