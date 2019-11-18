for n in range(100,1000):
	if n%37 == 0:
		x = n//100
		y = n//10 - x * 10
		z = n%100
		m = y * 100 + z * 10 + x
		p = z * 100 + x * 10 + y
		if m%37 != 0 or p%37 != 0:
			print('False')
			break
		else:
			print('True')