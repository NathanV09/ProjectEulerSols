#Since last digit is 0, the original number must end in a 0 and the second-to-last digit is also 0
#second to last digit must be either a 3 or a 7 to yield a 9
import datetime
a=datetime.datetime.now()
j=0
for i in range(int(10203040506070809**.5), int(19293949596979899**.5), 2):
    j=str(i**2)
    is_valid=True
    for k in range(0,len(j),2):
        if int(j[k]) != k/2+1:
            is_valid=False
            break
    if is_valid:
        print i, j
        break
b=datetime.datetime.now()
print (b-a)