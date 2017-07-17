import datetime
import math
a = datetime.datetime.now()
def number_rectangles(m, n):
    return n*(n+1)*m*(m+1)/4
target = 2*10**6
area = 0
min_dis_to_target = target
for i in range(1, 1414):
    for j in range(1, 1414):
        dis = math.fabs(number_rectangles(i, j)-target)
        if dis < min_dis_to_target:
            min_dis_to_target = dis
            area = i*j
            opt_i=i
            opt_j=j
        if number_rectangles(i, j) > target:
            break
print area
b = datetime.datetime.now()
print (b-a)
