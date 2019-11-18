n  = int(input('pls inut a number btw 1 to 9: '))

list1 = [x for x in range(1,101) if x%n != 0 and str(x).find(str(n)) == -1]
# list2 = [x for x in list1 if x%10 != n]
# list3 = [x for x in list2 if x//10 != n]

str1 = ''
count = 0

for i in list1:
	str1 = str1 + str(i) + ','
	count +=1
	if count % 10 ==0:
		print(str1)
		count = 0
		str1 = ''
if len(str1) > 0:
	print(str1)