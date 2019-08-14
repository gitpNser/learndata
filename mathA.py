# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:11:43 2019

@author: pNser copy Dazhuang@NJU
"""

import numpy as np
import pylab as pl
import scipy as sp


x = np.linspace(-np.pi, np.pi, 256)   #生成一系列线性的值，从-pi 到 pi
s = np.sin(x)
c = np.cos(x)
pl.title('Trigonometric Function')
pl.xlabel('X')
pl.ylabel('Y')
pl.plot(x,s)
pl.plot(x,c)

listA = sp.ones(500)
listA[100:300] = -1
f = sp.fft(listA)
pl.plot(f)
