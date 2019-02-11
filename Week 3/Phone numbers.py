#!/usr/bin/env python 
import sys
print("Enter a name and number, or a name and ? to query (!! to exit)")

phoneNumbersDict = {}

n = input()
while n != "!!":
	
	name, number = n.strip().split()

	if number == "?":
		try:
			print(name, "has number", phoneNumbersDict[name])
		except:
			print("Sorry, there is no", name)
	else:
		phoneNumbersDict[name] = int(number)

	n = input()

print("Bye")