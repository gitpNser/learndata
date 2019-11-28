# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:46:10 2019

@author: pNser
"""

with open('Blowing in the wind.txt', 'r+') as f:
    lines = f.readlines()
    lines.insert(0,'Blowing in the wind')
    lines.insert(1,'Bob Dylan')
    lines.append('1962 by Warner Bros. Inc.')
    lines = ''.join(lines)
    print(lines)
    f.seek(0)
    f.write(str(lines))
