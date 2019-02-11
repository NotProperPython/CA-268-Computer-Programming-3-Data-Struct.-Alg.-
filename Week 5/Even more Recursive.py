class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def count(self):
      return self.recursive_count(self.head)

    def recursive_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_count(ptr.next)

    def count_even(self):
        return self.rec_count_even(self.head)

    def rec_count_even(self, curr):
        if curr== None:
            return 0
        else:
            if int(curr.item) % 2 == 0:
                value = 1 
            else:
                value = 0
            return value + self.rec_count_even(curr.next)