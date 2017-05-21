import datetime
a = datetime.datetime.now()
def cube(n):
    return n**3
def sorted_number(n):
    digits = ''.join(sorted(str(n)))
    return digits
list_of_sorted_cubes=[]
for i in range(10000):
    list_of_sorted_cubes.append(sorted_number(cube(i)))
temp_list=[x for x in list_of_sorted_cubes]
list_of_sorted_cubes.sort()
sol_set=[]
for i in range(len(list_of_sorted_cubes)-4):
    if list_of_sorted_cubes[i]==list_of_sorted_cubes[i+1]:
        if list_of_sorted_cubes[i+2] == list_of_sorted_cubes[i + 1]:
            if list_of_sorted_cubes[i + 2] == list_of_sorted_cubes[i + 3]:
                if list_of_sorted_cubes[i + 3] == list_of_sorted_cubes[i + 4]:
                    for j in range(len(temp_list)):
                        if temp_list[j]==list_of_sorted_cubes[i]:
                            sol_set.append(j)
sol_set.sort()
print sol_set[0]**3
b = datetime.datetime.now()
print (b-a)