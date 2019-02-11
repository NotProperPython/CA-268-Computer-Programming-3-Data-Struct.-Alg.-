#!/usr/bin/env python3
class Stack:
#
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]

def check_brackets(line):
	S = Stack()
	check = []
	for i in line:
		if i == "(":
			S.push(i)
		elif i == ")":
			x = S.pop()
			if x == "(":
				continue
			else:
				S.push(x)
				check.append(i)

#	print(check)

	return S.is_empty() and len(check) == 0


	


def main():
	with open("test.txt", "r") as f:
		for i in f:
			print(check_brackets(i.strip()))

if __name__ == '__main__':
	main()