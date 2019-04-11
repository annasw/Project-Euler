# again, python does not have a problem handling big numbers
# (and 100! is way smaller than 2**1000)

from math import factorial

print(sum([int(i) for i in str(factorial(100))]))
