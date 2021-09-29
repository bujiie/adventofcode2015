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

p = (0,0)
M = {}
M[p] = 1
for i in ins:
    x,y = p
    dx,dy = d[i]
    xx = x + dx
    yy = y + dy

    if (xx,yy) not in M:
        M[(xx,yy)] = 1
    else:
        M[(xx,yy)] += 1
    p = (xx,yy)

print(len(M)) 
