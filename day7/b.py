#!/usr/bin/env python3

from sys import argv, getsizeof
import re

num_regex=r'\d+'

T={}
R={'b': 956}
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        
        expression, assignment=l.split(' -> ')
        terms=expression.split(' ')
       
        if len(terms)==1:
            if re.match(num_regex, terms[0]) is not None:
                R[assignment]=int(terms[0])
            else:
                T[assignment]=terms
        else:
            T[assignment]=terms

# override b AFTER initially populating R map
# otherwise it gets overriden and you end up with
# part 1 solution.
R['b']=956
done=set()
while len(done) < len(T):
    for t in T:
        op=None
        termz=[]
        all_num=True
        for tt in T[t]:
            if tt in ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']:
                op=tt
            else:
                if tt in R:
                    termz.append(R[tt])
                elif re.match(num_regex, tt) is not None:
                    termz.append(int(tt))
                else:
                    termz.append(tt)
                    all_num=False
        if all_num:
            done.add(t)
            if op=='AND':
                R[t]=termz[0] & termz[1]
            elif op=='OR':
                R[t]=termz[0] | termz[1]
            elif op=='LSHIFT':
                R[t]=termz[0] << termz[1]
            elif op=='RSHIFT':
                R[t]=termz[0] >> termz[1]
            elif op=='NOT':
                R[t]=~termz[0] & 65535
            else:
                R[t]=termz[0]
                         
                

print(R['a'])
    
        
         
