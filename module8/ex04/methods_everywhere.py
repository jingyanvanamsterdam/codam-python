#!/usr/bin/env python3

import sys
def shrink(str):
	x = slice(8)
	print(str[x])

def enlarge(str):
	l = len(str)
	i = l
	while i < 8:
		str += 'Z'
		i += 1
	print(str)

def func(args, p):
	i = 1
	while i <= p:
		l = len(args[i])
		if l == 8:
			print(args[i])
		elif l > 8:
			shrink(args[i])
		else:
			enlarge(args[i])
		i += 1

	
args = sys.argv
l = len(args)
if l == 1:
	print("none")
else:
	func(args, l - 1)