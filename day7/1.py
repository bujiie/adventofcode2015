#!/usr/bin/env python3

import fileinput
import re


E = {}
with fileinput.input() as fp:
    for line in fp:
        expression, variable = line.strip().split(" -> ")
        expression = expression.strip()
 
        if "AND" in expression:
            e = expression.replace(" AND ", "&")
        elif "OR" in expression:
            e = expression.replace(" OR ", "|")
        elif "NOT" in expression:
            e = expression.replace("NOT ", "~")
        elif " RSHIFT " in expression:
            e = expression.replace(" RSHIFT ", ">>")
        elif " LSHIFT " in expression:
            e = expression.replace(" LSHIFT ", "<<")
        else:
            e = expression

        E[variable] = "(" + e + ")"

done = set()
regex = r'[a-z]{1,}'
regex_group = r'([a-z]{1,})'
while len(done) < len(E):
    for variable in E:
        expression = E[variable]
        matches = re.findall(regex_group, expression)      

        if len(matches) == 0:
            done.add(variable)
            continue
       
        for match in matches:
            expression = re.sub(rf'([^a-z]){match}([^a-z])', rf'\1{E[match]}\2', expression)
        E[variable] = expression

         
print(E)                
        
    
