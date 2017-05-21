import datetime
a=datetime.datetime.now()
def brack_to_frac(array_of_nums):
    array_of_nums.reverse()
    num=0
    denom=1
    for i in array_of_nums:
        num+=i*denom
        temp=num
        num=denom
        denom=temp
    return [denom,num]
series=[2]
for i in range(1,100):
    if i%3!=2:
        series.append(1)
    else:
        series.append(2*(i+1)/3)
def num_to_sum(int):
    asum=0
    while int>0:
        asum+=int%10
        int/=10
    return asum
print num_to_sum(brack_to_frac(series)[0])
b=datetime.datetime.now()
print (b-a)