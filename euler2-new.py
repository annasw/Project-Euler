sum = 0
a = 1
b = 1

while a+b < 4000000:
	temp = a+b
	if temp%2==0: sum += temp
	a = b
	b = temp

print(sum)
