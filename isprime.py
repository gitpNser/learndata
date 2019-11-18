from math import sqrt

def isPrime(i):
	
	if i == 1:
		return False
	
	j = int(sqrt(i))
	
	for k in range(2, j+1):
		if i % k == 0:
			return False
	return True
	

for i in range(2,101):
	if isPrime(i):
		print(i, end = ' ')
	
			