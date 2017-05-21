def convert_to_bin(n):
	word=''
	for i in range(300):
		if 2**i>n:
			a=i
			break
	for i in range(a-1,-1,-1):
		if 2**i<=n:
			word+='1'
			n-=2**i
		else:
			word+='0'
	return word
for i in range(1,26):
    print i, convert_to_bin(10**i)