#!/usr/bin/env python3

from sys import argv
import re

lc=0
mc=0

regex=r'(\\\\|\\x[A-Za-z0-9]{2}|\\")'

with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        lc+=len(l)

        c=len(l)+4
        results=re.findall(regex, l[1:-1])
        if results is not None:
            for result in results:
                if result in ["\\\\", "\\\""]:
                    c+=2
                else:
                    c+=1
            
        mc+=c
print(mc-lc)
