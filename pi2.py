import itertools

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
	# pi1 = itertools.count(1)
	pi1 = itertools.count(1,2)
	# pi1 = itertools.takewhile(lambda x: x%2==1, pi1)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
	pi2 = itertools.takewhile(lambda x: (x <= 2*N), pi1)
	list1 = list(pi2)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
	list2 = [4/x * (2 - x%4) for x in list1]

    # step 4: 求和:
	
    return sum(list2)
	
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')