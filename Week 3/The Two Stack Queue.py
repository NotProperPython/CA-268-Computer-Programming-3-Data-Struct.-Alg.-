from Stack import Stack

class Queue:
    def __init__(self):
        self.enqstack = Stack()
        self.deqstack = Stack()
        self.size = 0

    def isempty(self):
        return self.enqstack.isempty() and self.deqstack.isempty()

    def enqueue(self, item):
        self.size += 1
        self.enqstack.push(item)

    def dequeue(self):
        self.size -= 1
        if not self.deqstack.isempty():
            return self.deqstack.pop()

        while not self.enqstack.isempty():
            self.deqstack.push(self.enqstack.pop())

        return self.deqstack.pop()