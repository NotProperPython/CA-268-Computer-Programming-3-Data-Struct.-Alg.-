#!/usr/bin/env python3
import sys

def set_stuff(s1, s2):

	union = s1.union(s2)
	subset = s1.issubset(s2)
	superset = s1.issuperset(s2)

	return union, subset, superset

