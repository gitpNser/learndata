import requests
import re
from bs4 import BeautifulSoup

r = requests.get('https://book.douban.com/subject/1084336/comments/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')
print(len(pattern))
i = 0
while i < 49:
	for item in pattern:
		# print(item.string)
		i +=1

pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)

ttl = 0
count = 0
while count < 49:
	for star in p:
		ttl += int(star)
		count +=1
print(i)
print(ttl)
print(count)
ave = ttl / count / 5
print('%.2f' % ave)