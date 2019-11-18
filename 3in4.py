n = 0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i != j and j != k and k !=i:
				n += 1
				print('%d' % (100 * i + 10 * j + k))
print(n)