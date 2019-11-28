import math

def is_prime(x):
	if x == 1:
		return False
	y = int(math.sqrt(x))
	for i in range(2, y+1):
		if x%i == 0:
			return False
	return True

def GC(n):
	k = 3
	while k < n:
		t = n - k
		if t < k:
			break
		if is_prime(k) and is_prime(t):
			return k, t
		k +=2

n = int(input('pls input a even number:'))
while n <200:
	print(is_prime(53))
	print(GC(n))

	if n > 4:
		a, b = GC(n)
		print(' %d = %d + %d' % (n, a, b))
	elif n==4:
		print(' %d = %d + %d' % (4, 2, 2))
	n +=2