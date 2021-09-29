#!/usr/bin/env python3

import fileinput
import re


vowels = r'[aeiou]'
repeat = r'.*(.)\1{1,}.*'
bad_strs = ['ab','cd','pq','xy']

lines = []
with fileinput.input() as fp:
	for line in fp:
		lines.append(line.strip())

def check(string):
	if len(re.findall(vowels, string)) > 2 and re.match(repeat, string):
		for bs in bad_strs:
			if bs in string:
				return False
		return True
	return False

count = 0
for line in lines:
	if check(line):
		count += 1

print(count)
