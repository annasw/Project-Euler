# there's PROBABLY a better way to do this just with powers
# like 1^n_0+2^n_1+... or something
# but i'd rather do it recursively
# even though obviously there are tricky aspects to doing it recursively
# i mean
# if you're stupid

amts = [200,100,50,20,10,5,2,1]

# return the number of ways that a number n can be made with english coins
# starting with a value of m, which initially is zero
# also x is the maximum value of coin you're allowed to use
# so we don't get repeats
# this makes sense and is sound and pythonic and... recursivic.
def numWays(n,m=0,x=200):
	if m>n: return 0
	if m==n: return 1
	
	tot = 0
	for e in amts:
		if e <= x: # avoid repeats please god
			tot += numWays(n,m+e,e)
	return tot
	
	# a worse attempt:
	'''
	tot = 0
	for e in range(len(amts[x:])): #AAAAAAAA
		tot += numWays(n,m+amts[e],e-1) #AAAAAAHHHHHHH
	return tot
	'''

print(numWays(200))
# oh god
# so also maybe there is an iterative solution
# but i'm going to sleep god dammit
