
data = []
count = 0
sum_len = 0
avg_len = 0
data_num = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %1000 除以1000後的餘數, ex: 7 % 3 = 1
			print(len(data))          
		length = len(line)
		sum_len = sum_len + length
		data_num = len(data)

		#print(sum_len)
		avg_len = sum_len / data_num
	

print('read finish, total are', len(data), 'data')
print('average length is', avg_len)

