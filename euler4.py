def isPalindrome(n):
	s = str(n)
	for i in range(len(s)):
		if s[i] != s[-(i+1)]:
			return False
	return True

largest = 0
for i in range(100,1000):
	for j in range(100,1000):
		if isPalindrome(i*j):
			largest = max(largest, i*j)

print(largest)
