# to make this slightly more efficient we're going to store paths
# in a hash table, key = start, val = # of steps from start to 1
# n.b. actually a significant timesave:
# w/ hashtable, runs in appx. 3.2 seconds
# w/out, runs in ~44.5 seconds.
# of course, we also end up using O(n) extra space, so... tradeoffs.

# takes a number n
# returns how many steps it takes to reduce n to 1 via the collatz sequence
# (might occasionally result in an infinite loop...)
def collatz(n, dict={}):
	count = 1 # irrelevant but apparently we're counting the starting # as a step
	while n > 1:
		# terminates as soon as we've hit a number we've seen before
		if n in dict:
			count += dict[n]
			break # i guess we could just return count here but break is more fun
				  # and honestly there's something pleasing to my coding mind about
				  # having exactly one return statement per method.
		
		if n%2==0:
			n /= 2
		else:
			n = (3*n)+1
		count += 1
	return count

d = {}
maxNum = 0
maxLen = 0
for i in range(1,1000000):
	x = collatz(i,d)
	d[i] = x
	if x > maxLen:
		maxLen = x
		maxNum = i

print(maxNum)
