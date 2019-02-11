#!/usr/bin/env python

def even_count(self):
	curr = self.head
	count = 0
	while curr is not None:
		if curr.item % 2 == 0:
			count +=1 
		curr = curr.next
	return count