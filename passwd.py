
correct = 'a123456'
times = 3
while times > 0:
	times = times - 1
	passwd = input('please input password:')
	if passwd == correct:
		print('password is correct')
		break
	else:
		print('password is error')
		if times > 0:
			print('you have', times, 'chance')
		else:
			print('you have no chance')