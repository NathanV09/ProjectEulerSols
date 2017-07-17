import datetime
a = datetime.datetime.now()
def digit_sum(n):
    n = str(n)
    dig_sum = 0
    for i in range(len(n)):
        dig_sum += int(n[i])
    n = int(n)
    return dig_sum

power_nums = []
for i in range(2, 70):
    for j in range(1, 35):
        res = i**j
        if res >= 10:
            if digit_sum(res) == i:
                power_nums.append(res)
power_nums.sort()
print power_nums[1]
print power_nums[9]
print power_nums[29]
b = datetime.datetime.now()
print (b-a)
