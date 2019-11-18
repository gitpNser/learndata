score = int(input('pls input the score:'))
if score > 100:
	print('invalid score,')
elif score >= 90:
	print('Grade is: A')
elif score >= 80:
	print('Grade is : B ')
elif score >=60:
	print('Grade is : C')
elif score >= 0:
	print('Grade is : D')
else:
	print('invalid score.')
	