# the math here is basically the following:
# the smallest number that's evenly divisible by some set of numbers s
# is a_0^p_0*a_1^p_1*...*a_n^p_n, where a_x is the xth prime factor
# and p_x is the maximum number of times it occurs for a single number in s
# thus this problem is trivial to answer with pen and paper
# but we can generalize an algorithm for any set s
# by just finding the prime factorization of each of the numbers in s
# and then comparing the greatest frequency with which each prime factor
# occurs for a single member of s...
# but instead i just did it "in my head" (i.e. in powershell) and it's

print(2*3*2*5*7*2*3*11*13*2*17*19)

# okay maybe i'll come back in a bit and do the actual coding work lol...
# but let's be real, the math and the answer are what matter for p.e.

# OKAY FINE

from math import sqrt, ceil

def isPrime(n):
	if n<2: return False
	if n==2	or n==3: return True
	if n%2==0: return False
	for f in range(3,ceil(sqrt(n))+1,2):
		if n%f == 0: return False
	return True

# generate a list of all the primes from 2 to n
# (or more accurately the largest prime <=n)
def genPrimes(n):
	primes = []
	for i in range(2,n+1):
		if isPrime(i):
			primes.append(i)
	return primes

# generate a list of the prime factors of n
def primeFac(n):
	p = genPrimes(n)
	factors = []
	for i in p:
		while n%i==0:
			factors.append(i)
			n/=i
	return factors

s = [i for i in range(1,21)]

d = {}
for x in s:
	p = primeFac(x)
	for i in set(p):
		d[i] = max(d.get(i,0),p.count(i))

prod = 1
for i in d:
	prod *= (i ** d[i])

print(prod)
