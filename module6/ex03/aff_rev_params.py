#!/usr/bin/env python3

import sys

args = sys.argv
l = len(args)
if l < 3:
	print("none")
else:
	while l > 1:
		print(args[l - 1])
		l -= 1

