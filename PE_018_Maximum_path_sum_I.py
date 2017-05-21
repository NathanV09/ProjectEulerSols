import _csv
with open("PE_67_Data.txt",'r') as f:
    data=list((_csv.reader(f, delimiter=" ")))
for line in data:
    for i in range(len(line)):
        line[i]=int(line[i])
data.reverse()
for i in range(1, len(data)):
    for j in range(0,len(data[i])):
        data[i][j]+=max(data[i-1][j],data[i-1][j+1])
print data[len(data)-1]