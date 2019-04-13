# i'm betting there's a really nice efficient way of computing the nth fibonacci #
# but idk what it is...
# it seems like one of those problems that's either super trivial
# or deceptively IMPOSSIBLE
# so im gonna just solve it the naive way and then look into better strats.

# update: so there's a formula but it's weird & i don't even know why i thought
# it would help. this is fine.

# we're gonna set it up s.t. a>b always bc that's more convenient for me
a = 1
b = 1
idx = 2
while len(str(a))<1000:
	c = a
	a = a+b
	b = c
	idx += 1
print(idx)
