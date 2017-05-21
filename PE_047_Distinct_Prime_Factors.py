import datetime
list_of_primes=[2]
for p in range(3,300000):
    max_p=p**.5
    for i in list_of_primes:
        if i > max_p:
            list_of_primes.append(p)
            break
        if p%i==0:
            break
a=datetime.datetime.now()
number_of_factors=[0]*300000
for p in list_of_primes:
    for i in range(0,len(number_of_factors),p):
        number_of_factors[i]+=1
for i in range(len(number_of_factors)-3):
    if number_of_factors[i]==4:
        if number_of_factors[i+1]==4:
            if number_of_factors[i+2]==4:
                if number_of_factors[i+3]==4:
                    print i
                    break
b=datetime.datetime.now()
print (b-a)