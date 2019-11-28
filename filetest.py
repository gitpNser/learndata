with open(r'd:\work\companies.txt') as f1:
	cNames = f1.readlines()
	for i in range(0, len(cNames)):
		cNames[i] = str(i+1) + '' + cNames[i]
s = '5Tencent Company'
with open(r'd:\work\scompanies.txt', 'a+') as f2:
	f2.writelines(cNames)
	f2.writelines('\n')
	f2.writelines(s)
	f2.seek(0)
	sName = f2.readlines()
	print(sName)
