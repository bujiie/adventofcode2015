#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	ins = fp.readline().strip()

	f = 0
	for c in ins:
		if c == '(':
			f += 1
		else:
			f -= 1

	print(f)
