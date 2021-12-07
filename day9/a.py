#!/usr/bin/env python3

from sys import argv
import re

D={}
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        f,t,d=re.split(' to | = ', l)
        if f not in D:
            D[f]={dest: t, dist: int(d)}

T={}
for d in D:
    :q


V=set()


