import datetime
def area_is_integer(a,b):
	#a,a,b
	s= a + b/float(2)
	area = (s-a)*((s-b)*s)**.5
	return (area%1==0)
total_sum=0
a=datetime.datetime.now()
for i in range(2,33333334):
	if area_is_integer(i,i-1):
		total_sum+=3*i-1
		print i,i,i-1
	if area_is_integer(i,i+1):
		total_sum+=3*i+1
		print i,i,i+1
print total_sum
b=datetime.datetime.now()
print (b-a)