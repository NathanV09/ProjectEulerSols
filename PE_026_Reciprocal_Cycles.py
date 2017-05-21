import datetime
c=datetime.datetime.now()
primes=[2]
for p in range(3,1000):
    max_p=p**.5
    for i in primes:
        if i>max_p:
            primes.append(p)
            break
        if p%i==0:
            break
maxmax_b=0
max_a=0
for a in primes:
    max_b=0
    for b in range(1, a):
        if (10**b-1)%a==0:
            max_b=b
            break
    if max_b>maxmax_b:
        maxmax_b=max_b
        max_a=a
print max_a
d=datetime.datetime.now()
print (d-c)