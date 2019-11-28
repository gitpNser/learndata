import requests
import re
import json
import pandas as pd
from datetime import date
import time
#from bs4 import BeautifulSoup

def retrieve_quotes_historical(stock_code):
	
	quotes = []
	
	url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
	r = requests.get(url)
	
	m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
	# m = re.findall('"historical-prices" data-reactid="33">(.*?)</table>', r.text)
	# print(m)
	
	# soup = BeautifulSoup(r.text, 'lxml')
	# m = soup.find_all('historical-prices')
	# print(m)
	
	
	if m:
		quotes = json.loads(m[0])
		quotes = quotes[::-1]
	return [item for item in quotes if not 'type' in item]
	
def create_df(stock_code):
	
	quotes = retrieve_quotes_historical(stock_code)
	
	list1 = []
	for i in range(len(quotes)):
		x = date.fromtimestamp(quotes[i]['date'])
		y = date.strftime(x, '%Y-%m-%d')
		list1.append(y)
			
	quotesdf_ori = pd.DataFrame(quotes, index = list1)
	
	listtemp = []
	for i in range(len(quotesdf_ori)):
		temp = time.strptime(quotesdf_ori.index[i], "%Y-%m-%d")
		listtemp.append(temp.tm_mon)
		
	tmpdf = quotesdf_ori.copy()
	tmpdf['month'] = listtemp
	
	totalclose = tmpdf.groupby('month').close.mean()
	df_totalclose = pd.DataFrame(totalclose)
	df_totalclose['code'] = stock_code
	
	return df_totalclose

# print(retrieve_quotes_historical('AXP'))
	
#dfAXP_totalclose = create_df('AXP')
#dfKO_totalclose = create_df('KO')
#AKdf = dfAXP_totalclose.append(dfKO_totalclose)
#AKdf['month'] = AKdf.index
#print(AKdf)

msft_close_mean = create_df('MSFT')
print(msft_close_mean)