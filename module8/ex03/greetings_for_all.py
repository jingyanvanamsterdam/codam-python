#!/usr/bin/env python3

def greetings(name="noble stranger"):
	if isinstance(name, int) == True:
		print("Error! It was not a name.")
	else:
		print(f"Hello, {name}")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)