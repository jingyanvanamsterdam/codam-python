#!/usr/bin/env python3

stop = "STOP"
w = input("What you gotta say? : ")
while w:
	if w == stop:
		break
	else:
		w = input("I got that! Anything else? : ")
