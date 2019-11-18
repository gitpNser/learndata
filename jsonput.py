import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
		
s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))

obj = dict(name='小明', age=20)
p = json.dumps(obj, ensure_ascii=False)
print(p)
