import datetime
def cant_touch_this(a,b):
	#a>b
	return 2*a**2+2*a*b
def is_relatively_prime(a,b):
	if a==1 or b==1:
		return True
	elif a==0 or b==0:
		return False
	else:
		return is_relatively_prime(b,a%b)
a = datetime.datetime.now()
triples=[0]*1500001
modular=[0]*1500001
for n in range(1,1300):
	for m in range(n+1,1300,2):
		if is_relatively_prime(m,n):
			if cant_touch_this(m,n) <=1500000:
				triples[cant_touch_this(m,n)]+=1
				modular[cant_touch_this(m,n)]+=1
b = datetime.datetime.now()
print (b-a)
for i in range(len(modular)):
	if modular[i]>0:
		for j in range(2, 1500000/i+3):
			if i*j<=1500000:
				triples[i*j]+=1
c=datetime.datetime.now()
print (c-b)
counter=0
for i in triples:
	if i==1:
		counter+=1
print counter
for i in range(150):
	if triples[i]==1:
		print i
print triples[48]