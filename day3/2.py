#!/usr/bin/env python3

import fileinput

ins = []
with fileinput.input() as fp:
    ins = list(fp.readline().strip())

d = {
    '^': (0,1),
    '>': (1,0),
    '<': (-1,0),
    'v': (0,-1)
}

p1 = (0,0)
p2 = (0,0)

M = {}
M[p1] = 2
for i, direction  in enumerate(ins):
    p = p1 if i % 2 == 0 else p2

    x,y = p
    dx,dy = d[direction]
    xx = x + dx
    yy = y + dy

    if (xx,yy) not in M:
        M[(xx,yy)] = 1
    else:
        M[(xx,yy)] += 1
    if i % 2 == 0:
        p1 = (xx,yy)
    else:
        p2 = (xx,yy)

print(len(M)) 
