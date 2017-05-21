min_difference = 9999999999
pentagonal_list=[]
for n in range(1,5000):
	pentagonal_list.append(((n)*(3*n-1)/2))
for a in range(1000):
	for i in range(1,a/2):
		if pentagonal_list[i]+pentagonal_list[a-i] in pentagonal_list:
			if pentagonal_list[a-i]-pentagonal_list[i] in pentagonal_list:
				difference=pentagonal_list[a-i]-pentagonal_list[i]
				if difference < min_difference:
					min_difference=difference
					print min_difference