import _csv
import datetime
a=datetime.datetime.now()
with open("PE_42_Data.txt",'r') as f:
    data=list(_csv.reader(f, delimiter=','))
triangle=[]
for i in range(40):
    triangle.append(i*(i+1)/2)
counter=0
print data
for thingy in data:
    for word in thingy:
        score=0
        for ltr in word:
            score+=ord(ltr)-64
        if score in triangle:
            counter+=1
print counter
b=datetime.datetime.now()
print (b-a)