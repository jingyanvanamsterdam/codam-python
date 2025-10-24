#!/usr/bin/env python3

i = 0
print("heloo")
while i in range(11):
	print(f"Table of {i}:", end = ' ')
	j = 0
	while j in range(11):
		print(i * j, end = ' ')
		j += 1
	print()
	i += 1

# if using for
#for i in range(11):
#	res = [str(i * j) for j in range(11)]
#	print(f"Table of {i}: {' '.join(res)}")