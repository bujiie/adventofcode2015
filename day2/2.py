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
	s = [l,w,h]
	s.sort()

	per = 2*(s[0]+s[1])
	vol = l*w*h
	t += (per+vol)

print(t)





