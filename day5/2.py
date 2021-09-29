#!/usr/bin/env python3

import fileinput
import re


lines = []
with fileinput.input() as fp:
	for line in fp:
		lines.append(line.strip())

rep_pairs = r'.*?(..)(?:.*?\1)+.*?'
rep_one = r'.*?(.).\1.*?'

def check(string):
	if re.match(rep_pairs, string) and re.match(rep_one, string):
		return True
	return False

count = 0
for line in lines:
	if check(line):
		count += 1

print(count)
