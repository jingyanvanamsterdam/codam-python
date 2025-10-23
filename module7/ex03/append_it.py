#!/usr/bin/env python3

import sys

def append_it(args):
	l = len(args)
	i = 1
	key = "ism"
	while i < l:
		if args[i].find(key) == -1:
			print(args[i] + key)
		i += 1

args = sys.argv
if len(args) == 1:
	print("none")
else:
	append_it(args)