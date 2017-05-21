import datetime
a = datetime.datetime.now()
counter = 0
maximum = 18000000
for i in range(1,maximum+1):
    i=str(i)
    temp1= [x for x in i]
    temp2=[x for x in temp1]
    temp2.sort()
    temp3=[x for x in temp2]
    temp3.reverse()
    if temp1!=temp2 and temp1!=temp3:
        counter += 1
    if counter/float(i) == .99:
        print counter, i
        break
b = datetime.datetime.now()
print (b-a)