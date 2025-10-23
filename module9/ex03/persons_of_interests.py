#!/usr/bin/env python3

def famous_births(women):
	lst = women.values()
	arr = sorted(lst, key=lambda d: d['date_of_birth'])
	i = 0
	while i < len(arr):
		print(f"{arr[i]['name']} is a greate scientist born in {arr[i]['date_of_birth']}")
		i += 1

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)