import requests, re
# from bs4 import BeautifulSoup

# stock_lst = []

# # try:
	# # r = requests.get('https://money.cnn.com/data/dow30/')
# # except Exception as err:
	# # print(err)
	# # break

# r = requests.get('https://money.cnn.com/data/dow30/')
	
# soup = BeautifulSoup(r.text, 'lxml')

# code = soup.find_all('a', 'wsod_symbol')
# name = soup.find_all('span','title')
# price = soup.find_all('span', 'wsod_stream')

# for item in price:
	# print(item.string)

# print(stock_lst)

def get_dw30():
	
	r = requests.get('https://money.cnn.com/data/dow30/')

	search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
	
	#'class="wsod_symbol">(.*?)<\/a>.*?   匹配class="wsod_symbol及</a>之间的任何文本
	#<span.*?">(.*?)<\/span>.*?  匹配 <span 以及有多个"的> 及 </span>之间的任何文本，
	#\n.*?class="wsod_stream">(.*?)<\/span> 匹配 class="wsod_stream及 </span>之间的任何文本，回车键没有理解
	
	
	dw30_list = re.findall(search_pattern, r.text)
	
	return dw30_list

dw30_list_text = get_dw30()
print(dw30_list_text)
	