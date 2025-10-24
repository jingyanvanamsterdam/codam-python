#!/usr/bin/env python3

try:
	n = int(input("Enter a number less than 25\n"))
	if n > 25:
		print("Error")
	else:
		i = 0
		while i <= 25 - n:
			print(f"Inside the loop, my variable is {n + i}")
			i += 1
except ValueError:
	print("Error")