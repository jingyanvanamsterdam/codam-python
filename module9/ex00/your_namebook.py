#!/usr/bin/env python3

def array_of_name(persons):
	arr = []
	for p in persons:
		first = p.capitalize()
		second = persons[p].capitalize()
		arr.append(first + ' ' + second)
	return arr


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_name(persons))