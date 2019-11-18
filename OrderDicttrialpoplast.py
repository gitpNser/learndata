from collections import OrderedDict 

class LastUpdatedOrderedDict(OrderedDict):

	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity
	
	def __setitem__(self, key, value):
		containskey = 1 if key in self else 0
		if len(self) - containskey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containskey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)
		
od1 = LastUpdatedOrderedDict(2)

od1['1'] = 'a'
od1['2'] = 'b'
od1['3'] = 'c'
od1['4'] = 'd'
od1[input('pls key in key: ')] = input('pls key in key value: ')

print(od1)

# print(od1)
# print(LastUpdatedOrderedDict)

# od1.setitem('a', 1)
# od1.setitem('b', 2)
# od1.setitem(input,input)
# print(list(od1.keys(), '=>', od1.values()))	