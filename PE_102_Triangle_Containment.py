# Let O = (0,0). Strategy: if [ABC] = [AOB]+[BOC]+[COA], return true, else, return false
import math
import _csv
import datetime
a = datetime.datetime.now()


def area(x1, y1, x2, y2, x3, y3):
    # returns the area of the triangle with the above vertices. Uses the shoelace area formula
    return .5*math.fabs((x1*y2+x2*y3+x3*y1)-(y1*x2+y2*x3+y3*x1))
with open("PE_102_Data.txt", 'r') as f:
    data = list(_csv.reader(f, delimiter=','))
for triangle in data:
    for i in range(len(triangle)):
        triangle[i] = int(triangle[i])
contain_counter = 0
for i in range(len(data)):
    abc = area(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5])
    aob = area(data[i][0], data[i][1], 0, 0, data[i][2], data[i][3])
    boc = area(data[i][2], data[i][3], 0, 0, data[i][4], data[i][5])
    coa = area(data[i][4], data[i][5], 0, 0, data[i][0], data[i][1])
    if abc == aob + boc + coa:
        contain_counter += 1
print contain_counter
b = datetime.datetime.now()
print (b-a)
