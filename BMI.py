weight, height = eval(input(' pls input weight and height: '))
BMI = weight / (height ** 2)
if BMI > 28:
	print('your BMI is %.2f' % BMI + ' fat')
elif BMI > 24:
	print('your BMI is %.2f' % BMI + ' over weight')
elif BMI > 18.5:
	print('your BMI is %.2f' % BMI + ' normal')
else:
	print('your BMI is %.2f' % BMI + ' too thin')