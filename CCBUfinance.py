# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:23:44 2019

@author: pNser
"""
import pandas as pd
import xlrd
import pymysql
from sqlalchemy import create_engine

file = 'CCBU report 201908.xlsx'

wb = xlrd.open_workbook(file)

sheets = wb.sheet_names()

df_CCBU = pd.read_excel(file,sheet_name=sheets[0],index_col=0)

#conn = pymysql.connect(
#        host='localhost',
#        user='finance',
#        password='test47',
#        db='finance',
#        port=3306,
#        charset='utf8mb4')

engine = create_engine('mysql+pymysql://finance:test47@localhost:3306/finance')

con = engine.connect()

df_CCBU.to_sql(name='CCBU', con=con, if_exists='append', index=False)



print(df_CCBU)
    
