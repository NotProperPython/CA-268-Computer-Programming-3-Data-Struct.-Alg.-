#!/usr/bin/env python 
import sys
def get_counts_dict(l):
    count = {}
    for i in l:
        if len(i) in count:
            count[len(i)] += 1
        else:
            count[len(i)] = 1
    return count 