# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:36:24 2019

@author: copied from dazhuang@NJU
"""

while True:
    try:
        qty = int(input('pls input the quantity of the goods:'))
        price = float(input('pls input the price of the goods:'))
        payment = qty * price
        print('the payment is: %.2f' % payment)
        break
    except Exception as err:
        print(err)
        print('pls re-try again!')
    
