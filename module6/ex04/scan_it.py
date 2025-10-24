#!/usr/bin/env python3

import sys
import re

args = sys.argv

p = len(args) - 1

if p != 2:
	print("none")
else:
	key = args[1]
	res = len(re.findall(key, args[2]))
	if res == 0:
		print("none")
	else:
		print(res)