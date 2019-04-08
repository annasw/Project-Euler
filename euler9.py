# we can (probably) do this more cleanly with math
# but it's really not that dirty this way either

def findTrip():
	for a in range(1, 333):
		for b in range(a+1, 500):
			c = 1000-a-b
			if c>b and c**2 == a**2 + b**2:
				return a*b*c

if __name__ == "__main__":
	print(findTrip())
