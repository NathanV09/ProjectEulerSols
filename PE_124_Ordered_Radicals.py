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
list_of_primes = sieve_for_primes_to(10**5)
for i in range(len(list_of_primes)):
    list_of_primes[i]=2*i*list_of_primes[i]+1
list_of_primes[0]=2
list_of_primes = [x for x in list_of_primes if x!=1]
factors=[[] for i in range(10**5+1)]
for p in list_of_primes:
    for i in range(p,10**5+1,p):
        factors[i].append(p)
for i in range(len(factors)):
    prod=1
    for f in factors[i]:
        prod*=f
    factors[i]=prod
new_factors=[x for x in factors]
factors.sort()
print new_factors
rad=factors[10000]
print rad
print factors
print new_factors.index(rad)