#!/usr/bin/env python3
import sys

def get_sliced_lists(l):
	sliced_lists = []
	sliced_lists.append(l[:-1])
	sliced_lists.append(l[1:-1])
	sliced_lists.append(l[::-1])
	return sliced_lists




def main():
    # read the list from stdin
    nums = []
    num = int(input())
    while num != -1:
        nums.append(num)
        num = int(input())
        
    # call the student's function with the list of numbers and ...
    lists = get_sliced_lists(nums)
    # ... print the result
    for lst in lists:
        print(lst)

if __name__ == "__main__":
    main()