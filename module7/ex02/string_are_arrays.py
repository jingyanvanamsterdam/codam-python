#!/usr/bin/env python3

import sys

def find_z(arg):
	l = len(arg)
	i = 0
	f = 0
	while i < l:
		if arg[i] == 'z':
			print("z", end="")
			f = 1
		i += 1
	if f == 0:
		print("none")

args = sys.argv
if len(args) == 1:
	print("none")
else:
	find_z(args[1])