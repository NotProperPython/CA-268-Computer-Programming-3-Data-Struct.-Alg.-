#!/usr/bin/env python3
import sys

def get_evenodd_list():
	odd_list = []
	even_list = []
	for num in sys.stdin:
		if int(num) == -1:
			break

		elif int(num) % 2 == 0:
			even_list.append(int(num.strip()))

		elif int(num) % 2 != 0:
			odd_list.append(int(num.strip()))
		

	return odd_list, even_list

def main():
    # call the get_odd_list function and print the result
    odds, evens = get_evenodd_list()
    print(odds)
    print(evens)

if __name__ == "__main__":
    main()