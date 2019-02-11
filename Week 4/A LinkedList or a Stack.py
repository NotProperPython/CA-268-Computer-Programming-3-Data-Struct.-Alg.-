from LinkedList import LinkedList

class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.add(item)

    def pop(self):
        return self.ll.remove()

    def is_empty(self):
        return self.ll.is_empty()