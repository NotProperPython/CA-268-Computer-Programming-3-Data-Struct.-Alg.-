import sys
def reverse_input(s):
	n = sys.stdin.readlines()
	for i in n:
		s.push(i.strip())

	while not s.is_empty():
		print(s.pop())