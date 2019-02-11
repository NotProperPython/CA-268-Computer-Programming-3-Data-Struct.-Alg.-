#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these functions are called methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def __str__(self):
            tmp_str = ""
            ptr = self.head
            while ptr != None:
                tmp_str += ptr.item + " "
                ptr = ptr.next
                
            return tmp_str

    def count(self):
        curr = self.head
        total = 0
        while curr is not None:
            total+=1
            curr = curr.next
        return total

    def contains(self, token):
        curr = self.head
        while curr is not None:
            if curr.item == token:
                return True
            curr = curr.next
        return False

    def after(self, token):
        curr = self.head
        while curr is not None:
            if curr.item == token:
                curr = curr.next
                return curr.item
            curr = curr.next
        return None

    def before(self, token):
        if self.head is not None:
            curr = self.head
            goal = None
            while curr is not None:
                if curr.item == token:
                    return goal

                goal  = curr.item
                curr = curr.next

            return None

    def append(self, item):
        if self.is_empty():
            self.add(item)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(item, None)

    def rotate(self):
        if self.is_empty():
            return None
        else:
            curr = self.remove()
            self.append(curr)