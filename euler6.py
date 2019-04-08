# the sum of the first 100 numbers is trivially 5050 (101*50)
# probably there is a clever math way to do this problem
# but the program is easy enough as it is
# (we also could have done a list comp for the sum but, again, trivial)

print(5050**2 - sum([n**2 for n in range(1,101)]))

# the dual list comp would have looked like

print(sum([n for n in range(1,101)])**2 - sum([n**2 for n in range(1,101)]))
