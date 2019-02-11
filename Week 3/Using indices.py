#!/usr/bin/env python3
import sys

def get_counts(l):
	count = [0,0,0,0,0,0,0,0,0,0]

	for i in l:
		count[len(i)] += 1

	return count




import sys
from numbers import get_counts

def main():
    # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()

    # call the student's function and ...
    counts = get_counts(words)
    # ... print the result
    for length in range(10):
        print(str(length) + ": " + str(counts[length]))

if __name__ == "__main__":
    main()