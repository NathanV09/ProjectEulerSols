import itertools
import datetime
t1=datetime.datetime.now()
perm_list=list(itertools.permutations([0,1,2,3,4,5,6,7,8,9],10))
def get_dig_to_num(array):
    num=0
    for i in array:
        num*=10
        num+=i
    return num
nums_sum=0
for i in perm_list:
    if i[5]==0 or i[5]==5:
        if get_dig_to_num(i[7:10])%17==0:
           if get_dig_to_num(i[6:9])%13==0:
               if get_dig_to_num(i[5:8])%11==0:
                   if get_dig_to_num(i[4:7])%7==0:
                       if get_dig_to_num(i[2:5])%3==0:
                           if i[3]%2==0:
                                nums_sum+=get_dig_to_num(i)
print nums_sum
t2=datetime.datetime.now()
print (t2-t1)