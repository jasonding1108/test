
#使用random來產生隨機整數

import random 

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('please input number:')
	num = int(num)

	if num == r:
		print('yor are correct')
		print('this is', count, 'times')
		break
	elif num > r:
		print('bigger than answer')
	elif num < r:
		print('smaller than answer')
	print('this is', count, 'times')