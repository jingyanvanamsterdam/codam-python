#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(arr)
arr = [x + 2 for x in arr if x > 5]
s = set(arr)
print(s)