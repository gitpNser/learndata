# _*_ coding:utf-8 _*_
"""
Get djidf

@author: copy from Dazhuang
"""

import requests
import re
import pandas as pd

def get_dji_list():
	
	try:
		r = requests.get('http://money.cnn.com/data/dow30/')
	except ConnectionError as err:
		print(err)
	
	search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
	
	dji_list_in_text = re.findall(search_pattern, r.text)
	
	dji_list = []
	for item in dji_list_in_text:
		dji_list.append([item[0],item[1],float(item[2])])
	
	return dji_list

dji_list = get_dji_list()
djidf = pd.DataFrame(dji_list)
columns = ['code', 'name', 'lasttrade']
index = range(1,len(djidf)+1)
djidf.columns = columns
djidf.index = index
print(djidf)