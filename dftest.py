# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:50:02 2019

@author: pNser
"""
import pandas as pd

music_data = [("the rollinng stones","Satisfication"),("Beatles","Let It Be"),("Guns N Roses","Don't cry"),("Metallica","Nothing Else Matters")]

columns = ['Singer','Song_name']

music_df = pd.DataFrame(music_data, columns =columns,index=range(1,5))

print(music_df)
