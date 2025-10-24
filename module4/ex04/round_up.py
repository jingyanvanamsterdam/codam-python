#!/usr/bin/env python3

try:
	num = float(input("Give me a number: "))
	if num.is_integer():
		num = int(num)
	elif num > 0:
		num = int(num) + 1
	else:
		num = int(num) - 1
	print(f"{num}")
except ValueError:
	print("Give a number.")