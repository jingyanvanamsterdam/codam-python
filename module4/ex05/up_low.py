#!/usr/bin/env python3

for c in input():
	if c.isupper() == True:
		print(f"{c.lower()}", end="")
	elif c.islower() == True:
		print(f"{c.upper()}", end="")
	else:
		print(f"{c}", end="")