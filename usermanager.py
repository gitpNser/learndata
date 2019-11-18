def newuser():
	username = input('pls input your name:')
	if user.get(username) is not None:
		print('username exist. pls input a new username:')
		newuser()
	else:
		password = input('pls input your password:')
		user[username] = password
	
def olduser():
	username, password = eval(input('pls input your username and password:'))
	if user[username] == password:
		print('welcome %s' % username)
	else:
		print('pls input correct password:')
		olduser()

def login():
	option = str(input('pls input option code. N for newuser, O for olduser, E for exit:'))
	if option == "N":
		newuser()
	if option == "O":
		olduser()
	# if option == "E":
		# break
	
if __name__ == "__main__":
	user = {('test' : 'test')}
	login()