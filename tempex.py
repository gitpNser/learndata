def temp_exchange(fs):
	return 5/9 * (fs - 32)
	
# print(temp_exchange(100))

for i in range(0, 320, 20):
	print('F: %d => C: %.2f' % (i, temp_exchange(i)))