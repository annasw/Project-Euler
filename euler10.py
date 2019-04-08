# we've already got these nice functions from euler5

from math import sqrt, ceil

def isPrime(n):
	if n<2: return False
	if n==2	or n==3: return True
	if n%2==0: return False
	for f in range(3,ceil(sqrt(n))+1,2):
		if n%f == 0: return False
	return True

# generate a list of all the primes from 2 to n
# (or more accurately from 2 to the largest prime <=n)
def genPrimes(n):
	primes = []
	for i in range(2,n+1):
		if isPrime(i):
			primes.append(i)
	return primes

# regrettably, this is actually pretty slow (appx 7 seconds to run),
# albeit well within the range of what projecteuler is looking for (<1min, iirc).
# i know there are faster methods of literally everything i'm doing here
# (primality tests, prime generation, and even summing all primes below n)
# maybe i'll improve on this later.
if __name__ == "__main__":
	print(sum(genPrimes(2000000)))
