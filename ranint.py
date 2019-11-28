import random

with open(r'd:\work\random.txt', 'w+') as f:
	for i in range(0,500):
		f.writelines(str(random.randint(1,100)))
		f.writelines('\n')
	f.seek(0)
	data1 = f.readlines()

data1 = [data.strip() for data in data1]
setdata1 = set(data1)

lst1 = [0] * 101

for data in setdata1:
	c = data1.count(data)
	lst1[int(data)] = c

for i in range(len(lst1)):
	if lst1[i] == max(lst1):
		print(i)
