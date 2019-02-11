def detect_loop(l):
	if l.head != None:
		curr = l.head
		head = l.head
		while curr.next != None:
			if curr.next == head:
				return True
			curr = curr.next
		return False
	return False