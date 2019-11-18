from math import sqrt

def solveq(a,b,c):
	t = b**2-4*a*c
	if t > 0:
		print(' the solutions are x1 = %.2f, x2 = %.2f' % (((-b)-sqrt(t))/(2*a), ((-b)+sqrt(t))/(2*a)))
	elif t == 0:
		print('the soution is x= %.2f' % ((-b)/(2*a)))
	else:
		print('there is no real solution.')
		
a, b, c = eval(input('pls input the the 3 parameters of the equation: '))
solveq(a,b,c)