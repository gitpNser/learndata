import requests, re
# from bs4 import BeautifulSoup

def volleyball(url):
	
	lst = []
	
	try:
		r = requests.get(url)
	except reuqests.exceptions.RequestException as err:
		return err
	
	r.encoding = r.apparent_encoding
	
	pattern = re.compile('href="/en/vnl/2018/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
	
	# 'href="/en/vnl/2018/women/teams/.*?">(.*?)</a>  匹配 'href="/en/vnl/2018/women/teams/.*?">开头, </a>收尾的中间所有文本
	# </figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td> 匹配 </figcaption>之下(s+代表多个空白字符，包括换行 的</figure>之下（s+代表多个空白字符，包括换行）的<td>与</td>之间的所有文本
	# s+<td class="table-td-bold">(.*?)</td> 匹配前面的<td>空白之后的<td class="table-td-bold">与</td>之间的所有文本
	# \s+<td class="table-td-rightborder">(.*?)</td>') 匹配前面的<td>空白之后的<td class="table-td-rightborder">与</td>之间的所有文本
	
	p = re.findall(pattern, r.text)
	
	return p
	
if __name__ == "__main__":
	
	url = 'http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'

	result = volleyball(url)
	
	print(result)
	
	# soup = BeautifulSoup(r.text, 'lxml')
	
	# name = soup.find_all('figcaption')
	
	# total = soup.find_all('\div\table\tbody\tr\td')
	
	# won = soup.find_all('td', 'table-td-bold')
	
	# for item in won:
		# lst.append(item.string)
	
	# return lst
		
# url = 'http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
	
# vbranklist = volleyball(url)

# print(vbranklist)