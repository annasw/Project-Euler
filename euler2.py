fib = []
a,b = 1,1
while (a+b < 4000000):
	fib.append(a+b)
	c = a+b
	a = b
	b = c

sum = 0
for x in fib:
	if x%2 == 0: sum += x
print sum