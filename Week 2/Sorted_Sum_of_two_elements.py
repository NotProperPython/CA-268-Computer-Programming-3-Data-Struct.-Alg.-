#!/usr/bin/env python 

def sum_to_k(l, k):
	low = 0 
	high = len(l) -1
	while low < high:
		pair = l[low] + l[high]
		if pair < k:
			 low+=1
		elif pair > k:
			high -= 1
		else:
			return True
	return False