from itertools import permutations
import datetime
x1 = datetime.datetime.now()
list_of_primes=[2]
for p in range(3,10000):
    max_p=p**.5
    for i in list_of_primes:
        if i > max_p:
            list_of_primes.append(p)
            break
        if p%i==0:
            break
list_of_primes=[x for x in list_of_primes if x > 1000]
def dig_split(n):
    dig_list=[]
    while (n > 0):
        dig_list.append(n%10)
        n = n/10
    return dig_list
def dig_list_to_number(n):
    number = 0
    for i in n:
        number*=10
        number+=i
    return number
perm_list=[]
for i in list_of_primes:
        dig_list = dig_split(i)
        perms = list(permutations(dig_list,len(dig_list)))
        for j in range(len(perms)):
            perms[j]=dig_list_to_number(perms[j])
        perms = [x for x in perms if x in list_of_primes]
        perms.sort()
        for j in range(len(perms)-1):
            if perms[j]==perms[j+1]:
                perms[j]=0
        perms = [x for x in perms if x!=0]
        if len(perms) > 2 and perms not in perm_list:
            perm_list.append(perms)
for perm in perm_list:
    for a in range(len(perm)-2):
        for b in range(a+1, len(perm)-1):
            for c in range(b+1, len(perm)):
                if perm[a]+perm[c]==2*perm[b]:
                    print perm[a],perm[b],perm[c]
y1=datetime.datetime.now()
print (y1-x1)