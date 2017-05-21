import datetime
c=datetime.datetime.now()
alist=[]
for a in range(9000,10000):
    alist.append(int(str(a)+str(a*2)))
def num_to_array(num):
    array=[]
    while num>0:
        array.append(num%10)
        num/=10
    return array
def array_to_num(array):
    num=0
    for i in array:
        num*=10
        num+=i
    return num
for i in range(0, len(alist)):
    alist[i]=num_to_array(alist[i])
    alist[i].sort()
    alist[i]=array_to_num(alist[i])
for i in range(len(alist)):
    if alist[i]==123456789:
        print i
d=datetime.datetime.now()
print (d-c)