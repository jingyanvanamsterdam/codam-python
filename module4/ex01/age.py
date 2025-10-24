#!/usr/bin/env python3

try:
	age = int(input("Please tell me your age: "))
	print(f"You are currently {age} years old.")
	i = 1
	while i in range(1, 4):
		print(f"In {i * 10} years, you'll be {age + i * 10} years old.")
		i += 1;
except ValueError:
	print("Enter a number")