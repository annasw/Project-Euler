from math import sqrt, ceil

def isPrime(n):
	if n<2: return False
	if n==2	or n==3: return True
	if n%2==0: return False
	for f in range(3,ceil(sqrt(n))+1,2):
		if n%f == 0: return False
	return True

i = 600851475143
if isPrime(i): print(i)
else:
	for x in range(ceil(sqrt(i)),0,-1):
		if i%x==0 and isPrime(x):
			print(x)
			break
