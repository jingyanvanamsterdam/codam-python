#!/usr/bin/env python3

import sys

args = sys.argv

if len(args) != 3:
	print("none")
else:
	n1 = int(args[1])
	n2 = int(args[2])
	if n1 < n2:
		lst = [i for i in range(n1, n2 + 1)]
		print(lst)
	