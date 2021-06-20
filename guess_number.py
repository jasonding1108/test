
#使用random來產生隨機整數

import random 

r = random.randint(1, 100)

while True:
	num = input('please input number:')
	num = int(num)

	if num == r:
		print('yor are correct')
		break
	elif num > r:
		print('bigger than answer')
	elif num < r:
		print('smaller than answer')