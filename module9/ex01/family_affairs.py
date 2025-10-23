#!/usr/bin/env python3

def find_the_redhead(family):
	lst = list()
	for name in family.keys():
		if family[name] == "red":
			lst.append(name)
	return lst

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redhead(dupont_family))