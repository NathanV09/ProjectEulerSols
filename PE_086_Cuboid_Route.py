counter=0
for i in range(100):
    for a in range(1,i+1):
        for b in range(1,a+1):
            if (i**2+(a+b)**2)**.5 % 1 == 0:
                counter+=1
print counter