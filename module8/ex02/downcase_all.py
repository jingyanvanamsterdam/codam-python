#!/usr/bin/env python3

import sys

def downcase_it(str):
	return str.lower()

args = sys.argv
p = len(args) - 1
if p == 0:
	print("none")
else:
	i = 1
	while i <= p:
		print(downcase_it(args[i]))
		i += 1