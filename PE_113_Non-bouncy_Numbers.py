import math
import datetime
a=datetime.datetime.now()
def nCr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
counter=0
for i in range(100):
    for j in range(1,10):
        counter+=nCr(i+j,i)
for i in range(100):
    for j in range(9):
        counter+=nCr(i+j,i)
counter-=100*9
print counter
b=datetime.datetime.now()
print (b-a)