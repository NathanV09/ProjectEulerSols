import datetime
counter = 0
def is_relatively_prime(a,b):
    if a==1 or b==1:
        return True
    elif a==0 or b==0:
        return False
    else:
        return is_relatively_prime(b%a,a)
counter=0
a=datetime.datetime.now()
for d in range(1,1201):
    for n in range(int(d/float(3)), int(d/float(2))+1):
        if n > 0:
            if is_relatively_prime(d,n):
                if n/float(d) >= 1/float(3) and n/float(d) <= .5:
                    counter+=1
    print d, counter
print counter
b=datetime.datetime.now()
print (b-a)