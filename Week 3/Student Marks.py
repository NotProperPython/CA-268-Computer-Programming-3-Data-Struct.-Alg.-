#!/usr/bin/env python 
import sys
def make_map():
	studentsDict = {}
	for i in sys.stdin:
		if len(i.strip()) > 0:
			name, mark = i.strip().split()
			studentsDict[name] = mark
	return studentsDict