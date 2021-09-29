#!/usr/bin/env python3

import fileinput
import hashlib


hash = None
with fileinput.input() as fp:
	hash = fp.readline().strip()
	

res = None
i = 0
zeros = 6
while True:
	s = f'{hash}{str(i)}'
	h = hashlib.md5(s.encode())
	res = h.hexdigest()
	if res.startswith('0'*zeros):
		break;
	i += 1

print(i)
print(res)
