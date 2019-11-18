with open(r'd:\work\article.txt') as f:
	s = f.read()

words = s.split()
lst = []

for word in words:
	if word[-3:] == '...':
		word = word[:-3]
		lst.append(word)
	if word[-1] in ',.?!':
		word = word[:-1]
	lst.append(word)

result = sorted(lst, key=len, reverse = True)
maxlen = len(result[0])

# 以下取所有最长单词，同时去重
for word in set(result):
	n = len(word)
	if n == maxlen:
		print(word)