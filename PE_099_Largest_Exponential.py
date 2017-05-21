import _csv
import math
import datetime
a=datetime.datetime.now()
with open("PE_99_Data.txt",'r') as f:
    data = list(_csv.reader(f, delimiter=','))
for line in data:
    for i in range(len(line)):
        line[i] = int(line[i])
maximum = 0
line = 0
for i in range(len(data)):
    result = data[i][1]*math.log(data[i][0])
    if result > maximum:
        maximum = result
        line = i+1
print line
b=datetime.datetime.now()
print (b-a)
