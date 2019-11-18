def odd_t(n):
	if n % 2 == 0:
		return False
	else:
		return True


m = eval(input('pls input a number: '))

while m > 1:	
	if odd_t(m):
		print('%d * 3 + 1 = %d' % (m, m * 3 + 1))
		m = m * 3 + 1
	else:
		print('%d / 2 = %d' % (m, m/2))
		m = m / 2
