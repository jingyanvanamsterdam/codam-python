#!/usr/bin/env python3

try:
	a = int(input("Give me the first number: "))
	b = int(input("Give me the second number: "))
	print("Thank you!")
	print(f"{a} + {b} = {a + b}")
	print(f"{a} - {b} = {a - b}")
	print(f"{a} / {b} = {int(a / b)}")
	print(f"{a} * {b} = {a * b}")
except ValueError:
	print("Enter a number.")