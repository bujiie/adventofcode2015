#!/usr/bin/env python3

import fileinput

pres = []
with fileinput.input() as fp:
	for line in fp:
		l,w,h = list(map(lambda n: int(n), line.strip().split('x')))
		pres.append((l,w,h))

t = 0
for p in pres:
	l,w,h = p
	a = l*w
	b = w*h
	c = l*h
	e = min([a,b,c])

	t += (2*(a+b+c)+e)

print(t)





