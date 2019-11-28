def find_person(dict, strU):
	for k in dict:
		if k == strU:
			return dict[k]
	return 'Not Found'

		
if __name__ == '__main__':
	dict_users = {"xiaoyun" : 8888, "xiaohong" : 5555555, "xiaoteng" : 12341234, "xiaoyang" : 1212121}
	strU = input("pls input the person's name: ")
	print(find_person(dict_users, strU))