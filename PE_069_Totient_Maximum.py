list_of_primes = [2]
for p in range(3,10**6):
	for i in list_of_primes:
		if i > p**.5:
			list_of_primes.append(p)
			break
		if p%i==0:
			break
max_totient_ratio=0
max_i=0
factors_list=[i for i in xrange(10**6)]
for p in list_of_primes:
	for i in range(p,len(factors_list),p):
		factors_list[i]=int(factors_list[i]*(1-1/float(p)))
print factors_list[0:10]
for i in range(1,len(factors_list)):
	ratio = i/float(factors_list[i])
	if ratio > max_totient_ratio:
		max_totient_ratio=ratio
		max_i=i
print max_i