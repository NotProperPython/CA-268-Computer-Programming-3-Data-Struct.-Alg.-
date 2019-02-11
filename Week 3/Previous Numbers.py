#!/usr/bin/env python3
import sys

lst = []
dup_lst = []
num = input()
while int(num) != -1:
	if int(num) in lst:
		dup_lst.append(num)
	else:
		lst.append(int(num))
	num = input()
previous = " ".join(dup_lst)
print("Enter numbers (-1 to end):", " ".join(dup_lst)+ " ")