'''
Step inside the mind of a madwoman.
I solved this very quickly and then decided to do a one-liner solution.
Without using import statements.
I haven't quite figured it out yet, but um... there's some work in here.
I'm very close, it just doesn't quite work yet.
The working solution is pretty obvious, at the top, and after that you can stop reading.
Please.
'''

from math import factorial as f

# so the initial tricky thing here seems to be coming up with an upper bound
# because they want ALL such numbers
# and all is a big word.
# we're looking for the smallest number x, where x=99..9, s.t.
# 9!+9!+..+9! < x
# 9! = 362880, so an n-digit number can have a max sum-of-factorials-of-digits
# (henceforth SOFOD) of 362880n.
# anyway the answer is that you can have SOFOD(x)=x for 7-digit numbers,
# but not 8-digit numbers. so we go up to 9999999.

# takes an integer x
# returns the sum of the factorials of the digits of x
def SOFOD(x):
	return sum([f(int(i)) for i in str(x)]) #yass

total = 0
for i in range(3,10000000):
	if SOFOD(i)==i:
		total += i

print(total)

# okay so this takes some time to run (appx 26 seconds), which is... not great.
# and implies that there's probably a faster solution (quite possibly built
# around the factorials themselves rather than this naive approach.)
# but regardless.
# oh also fun fact: there are (somehow) only two such numbers:
# 145 and 40585. weird but evidently true.
# so it's possible my upper bound was a little high lmao.


# okay this person did a one-liner haskell solution and therefore NOT TO BE OUTDONE
#def f(x): return eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)])) if x!=0 else 1 # this is not the one-liner. everything from here on is insane and out of order. move along.

#print(sum([sum([f(int(i)) for i in str(x)]) for x in range(3,10000000) if sum([f(int(i)) for i in str(x)]) == x]))
# okay so this is the old one ^ but it works FINE with the imported f(n) but not with the one i wrote, even though the one i wrote DOES function properly in tests...
# okay so my defined f(x) works ONLY with integers >=1... and the other numerical inputs (e.g. 0, -1, 0.5) all throw EOF exceptions for some fucking reason
# so that might be it...
# yes: we're passing f(x) some zeroes as digits... and we need to return 1 there. god fucking dammit.

# (still not technically a one-liner because of the import statement,
# but if there's a way to code the factorial function in as part of this monstrosity
# i dont want to know it)

# sike yes i do LET'S GO

#print(sum([sum([eval('*'.join(str(e) for e in [t for t in range(x)])) for i in str(x)]) for x in range(3,10000000)]))

#def f(x): return eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)]))

# this is the original "one-liner":
#[sum([f(i) for i in str(x)]) for x in range(3,10000000) if sum([f(i) for i in str(x)]) == x]

# final eval:
#def f(x): return eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)])) if x!=0 else 1

# closest thing to working:
#######print(sum([sum([eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)])) if x!=0 else 1 for i in str(x)]) for x in range(3,150) if sum([eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)])) if x!=0 else 1 for i in str(x)]) == x]))
# so this produces 0 instead of 145 even with the range narrowed, and with a bigger range (for possibly the same reason) it throws a recursive depth exceeded exception, so idk figure that one out genius girl

#print(sum([sum([eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)])) if x!=0 else 1 for i in str(x)]) for x in range(3,10000000) if sum([eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)])) if x!=0 else 1 for i in str(x)]) == x]))


#print(sum([sum([eval('*'.join(str(e) for e in [t for t in range(1,int(i)+1)])) for i in str(x)]) for x in range(3,10000000) if sum([eval('*'.join(str(e) for e in [t for t in range(1,int(i)+1)])) for i in str(x)]) == x]))

# so replace f(int(i)) with:
#eval('*'.join(str(e) for e in [t for t in range(1,int(i)+1)]))
# this WORKS btw
# or at least THIS does:
# eval('*'.join(str(e) for e in [t for t in range(1,int(3)+1)]))
# we can also define a function
# def f(x): return eval('*'.join(str(e) for e in [t for t in range(1,int(x)+1)]))
# and that works fine as a factorial function
