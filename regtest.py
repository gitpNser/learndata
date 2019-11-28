import re

def is_valid_email(addr):
	if re.match(r'^\w[\w|\.]+@\w+\.com$', addr):
		return True
	else:
		return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
	
def name_of_email(addr):
	p = re.match(r'\<([\w\s]+)\>', addr)
	if p:
		return p.group(1)
	else:
		s = re.match(r'(^\w[\w|\.]+)@\w+[\.\w]+$', addr)
		return s.group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')