# _*_ coding: utf-8 _*_
def add(x, y, f):
	f = abs
	return f(x) + f(y)
print(add(-5, 6, abs))