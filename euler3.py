# solution for euler3
# has a bunch of methods i don't actually use
# the only ones i actually use are factorsImproved(x) and findPrime(x)

def findPrime(x):
	n = 2
	while n<((x/2)+1):
		if x%n == 0: return False
		n += 1
	return True
	
def topPrimeByPrimes(number):
	#primes = [1]
	n = ((number/2)+1)
	while n > 1:
		if findPrime(n)==True:
			if number%n == 0: return n
		n -= 1
	return 1

#def topPrimeByFactors(x):
#	factors = []
#	n = (x/2)+1
#	while n>1:
#		if x%n == 0:
#			if findPrime(n) == True: return n
#		n-=1
#	return 1

def factorsImproved(x):
	n = 2
	while n < ((x/2)+1):
		if x%n == 0:
			if findPrime(x/n) == True: return (x/n)
		n += 1
	return 1

def maxPrime(x):
	primes = listPrimes(x)
	for n in primes:
		if x%n == 0:
			return n
	return 1

while True:
	i = int(raw_input("> "))
	print factorsImproved(i)
