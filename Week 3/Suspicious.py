#!/usr/bin/env python3
import os
import sys
f1= sys.argv[1]
f2= sys.argv[2]

with open(f1, "r") as f:
	with open(f2, "r") as g:
		students_set = set([i.strip() for i in f])
		delinquents_set = set([i.strip() for i in g])

suspicious_lst = sorted(list(students_set & delinquents_set))

i = 0
while i < len(suspicious_lst):
	print("{}. {}".format(i+1, suspicious_lst[i]))
	i += 1