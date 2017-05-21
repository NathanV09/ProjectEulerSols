import datetime
a = datetime.datetime.now()
def base_ten_to_binary_list(n):
	lmaokai = True
	bin_list = []
	while (n>0):
		bin_list.append(n%2)
		n -=n%2
		n = n/2
	for i in range(len(bin_list)):
		if bin_list[i]!=bin_list[len(bin_list)-1-i]:
			lmaokai = False
			break
	return lmaokai
def base_ten_list(n):
	lol = True
	log_list = []
	while (n>0):
		log_list.append(n%10)
		n = n-n%10
		n = n/10
	for i in range(len(log_list)):
		if log_list[i]!=log_list[len(log_list)-1-i]:
			lol = False
			break
	return lol
sum = 0
for n in range(1000000):
	if base_ten_to_binary_list(n) and base_ten_list(n):
		sum +=n
print sum
b = datetime.datetime.now()
print (b-a)