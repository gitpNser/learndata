def normalize(name):
	name = name[0].upper() + name[1:].lower()
	return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def fn(x, y):
	return x * y
def prod(L):
	return reduce(fn, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
	
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    
def char2num(s):
    return DIGITS[s]
def fm(x, y):
	return x * 10 + y
def str2float(s):
	f,e = s.split('.')
	ff = reduce(fm, map(char2num, f))
	ee = reduce(fm, map(char2num, e))/pow(10,len(e))
	return ff + ee
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
    