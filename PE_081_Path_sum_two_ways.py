import _csv
import datetime
a=datetime.datetime.now()
with open("PE_81_Data.txt",'r') as f:
    data=list(_csv.reader(f, delimiter=","))
for line in data:
    for i in range(len(line)):
        line[i]=int(line[i])
for i in range(1,80):
    data[0][i]+=data[0][i-1]
for i in range(1,80):
    data[i][0]+=data[i-1][0]
for i in range(2,170):
    for j in range(1,i+1):
        try:
            data[j][i-j]+=min(data[j-1][i-j], data[j][i-j-1])
        except:
            pass
for line in data:
    print line
b=datetime.datetime.now()
print (b-a)