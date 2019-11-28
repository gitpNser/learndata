# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:02:22 2019

@author: pNser copy Dazhuang@NJU
"""
import random

def func(data):
    
    cls_no = random.choice(list(data.keys()))
    stu_no = random.randint(1,data[cls_no])
    
    return "{}:{:02}".format(cls_no,stu_no)

if __name__ == "__main__":
    
    data = {'A001':32,"A002":47,"B001":39,"B002":42}
    
    result = set()
    
    while len(result) < 10:
        result.add(func(data))
        
    print(result)
