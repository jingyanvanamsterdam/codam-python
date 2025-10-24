#!/usr/bin/env python3

try:
	n = int(input("Enter a number\n"))
	i = 0
	while i < 10:
		m = i * n
		print(f"{i} x {n} = {m}")
		i += 1
except ValueError:
	print("Error input.")