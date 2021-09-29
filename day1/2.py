#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	ins = fp.readline().strip()

	f = 0
	for i, d in enumerate(ins):
		if d == '(':
			f += 1
		else:
			f -= 1

		if f < 0:
			print(i+1)
			break

