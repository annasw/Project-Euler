# almost certain there's a cleaner math way to do this
# but it runs in a fraction of a second anyway

from math import sqrt, ceil

def isPrime(n):
	if n<2: return False
	if n==2	or n==3: return True
	if n%2==0: return False
	for f in range(3,ceil(sqrt(n))+1,2):
		if n%f == 0: return False
	return True

primeCount = 2 # 2 and 3
currNum = 3
while primeCount <= 10000:
	currNum += 2
	if isPrime(currNum):
		primeCount += 1

print(currNum)
