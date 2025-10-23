#!/usr/bin/env python3

import sys

args = sys.argv

def prompt(arg):
	pm = input("Wat was the parameter? ")
	if arg == pm:
		print("Good job!")
	else:
		print("Nope, sorry...")

if len(args) == 1:
	print("none")
else:
	prompt(args[1])