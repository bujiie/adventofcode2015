#!/usr/bin/env python3

import fileinput

G = {}
ins = []

def state(curr, cmd):
	if cmd == 'on':
		return curr + 1
	if cmd == 'off':
		return curr - 1 if curr > 0 else 0
	return curr + 2

with fileinput.input() as fp:
	for line in fp:
		s,e = line.strip().split('through')
		cmd = None
		offset = 0
		if s.startswith('turn on'):
			cmd = 'on'
			offset = len('turn on')
		elif s.startswith('turn off'):
			cmd = 'off'
			offset = len('turn off')
		else:
			cmd = 'toggle'
			offset = len('toggle')

		sx,sy = list(map(lambda n: int(n), s[offset:].strip().split(',')))
		ex,ey = list(map(lambda n: int(n), e.strip().split(',')))
		ins.append((cmd, sx,sy,ex,ey))		


	count = 0
	for cmd,sx,sy,ex,ey in ins:
		for x in range(sx, ex+1):
			for y in range(sy, ey+1):
				if (x,y) not in G:
					G[(x,y)] = False

				o_state = G[(x,y)]	
				n_state = state(o_state, cmd)
				G[(x,y)] = n_state
				count += (n_state - o_state)

	print(count)


		



