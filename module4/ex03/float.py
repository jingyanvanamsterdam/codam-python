#!/usr/bin/env python3

num = input("Give me a number: ")
try:
	float_num = float(num)
	if float_num.is_integer():
		print("This number is an integer.")
	else:
		print("This number is a decimal.")
except ValueError:
	print("Give a number.")



#if num.isdigit():
#	print("This number is an integer.")
#elif float(num):
#	print("This number is a decimal.")
#else:
#	print("Please enter a number.")
#print(f"{num.isdigit()}")
#print(f"num is {type(num)}") -- class str
#print(f"num is {isinstance(num, int)}") -- False
#print(f"num is {isinstance(num, float)}") -- False