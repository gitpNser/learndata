import re, requests, time
from bs4 import BeautifulSoup

count = 0
i = 0
j = 0
s, count_s, count_del = 0, 0, 0
lst_star = []

while count < 50:
	try:
		r = requests.get('https://book.douban.com/subject/1084336/comments/hot?p='+str(i+1))
	except Exception as err:
		print(err)
		break
	
	soup = BeautifulSoup(r.text, 'lxml')
	comments = soup.find_all('span', 'short')
	
	pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
	p = re.findall(pattern, r.text)
	
	for item in comments:
		count +=1
		if count > 50:
			# count the number of comments more than 50 of the page
			count_del +=1
		else:
			print(count, item.string)
	
	for star in p:
		lst_star.append(int(star))
	
	time.sleep(5)	# delay request from douban's robots.txt
	
	i +=1
	
	for star in lst_star[:-count_del]:	# calculate the rating star of 50 comments
		print(j+1, int(star))
		s += int(star)
		j +=1
		
if count >= 50:
	print(s // (len(lst_star)- count_del))
	print(len(lst_star))
	print(count_del)