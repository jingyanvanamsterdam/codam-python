#!/usr/bin/env python3

import sys

def count_it(args):
	l = len(args) - 1
	print(f"parameters: {l}")
	i = 1
	while i <= l:
		print(f"{args[i]}: {len(args[i])}")
		i += 1
		
args = sys.argv
count_it(args)