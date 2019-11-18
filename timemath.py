def time_o(n):
	if n == 1:
		return 1
	m = 1
	for i in range(1, n+1):
		m =  m * i
	return m
	
# print(time_o(2))

def time_n(n):
	if n == 1:
		return 1
	p = 0
	for i in range(1, n + 1):
		p = p + time_o(i)
	return p

q = eval(input('pls input a number: '))
print(time_n(q))

s = term = 1
for i in range(2, q + 1):
	term = term * i
	s = s + term
print(s)
	