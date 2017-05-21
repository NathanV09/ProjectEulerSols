import datetime
a=datetime.datetime.now()
def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return sieve
list_of_primes = sieve_for_primes_to(10**7)
for i in range(len(list_of_primes)):
	list_of_primes[i] = list_of_primes[i]*(2*i+1)
list_of_primes[0] = 2
list_of_primes = [x for x in list_of_primes if x!=0]
print list_of_primes[0:10]
b=datetime.datetime.now()
print (b-a)
factors_list=[i for i in xrange(10**7)]
print factors_list[0:10]
for p in list_of_primes:
	for i in range(p,len(factors_list),p):
		factors_list[i]*=(1-1/float(p))
for i in range(len(factors_list)):
	factors_list[i]=int(factors_list[i])
print factors_list[0:10]
min_ratio=5
min_n=0
for i in range(2,len(factors_list)):
	if ''.join(sorted(str(factors_list[i])))==''.join(sorted(str(i))):
		ratio=i/float(factors_list[i])
		if ratio<min_ratio:
			min_ratio=ratio
			print factors_list[i], i
c=datetime.datetime.now()
print (c-a)