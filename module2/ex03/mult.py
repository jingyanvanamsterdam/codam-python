#!/usr/bin/env python3

try:
	x = int(input("Enter the first number:\n"))
	y = int(input("Enter the second number:\n"))
	z = x * y
	print(f"{x} x {y} = {z}")
	if z < 0:
		print("The result is negative.")
	elif z > 0:
		print("The result is is positive.")
	else:
		print("The result is is positive and negative.")
except ValueError:
	print("Please enter a number!")