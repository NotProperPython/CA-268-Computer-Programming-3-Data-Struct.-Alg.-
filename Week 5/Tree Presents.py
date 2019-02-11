class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)
    def recursive_total(self, ptr):
      if ptr == None:
        return 0
      return self.recursive_total(ptr.left) + self.recursive_total(ptr.right) + ptr.item
      
    def total(self):
      return self.recursive_total(self.root)

    def is_present(self, arg):
        return self.rec_is_present(arg,self.root)

    def rec_is_present(self,arg,curr):
        if curr == None:
            return False
        elif curr.item == arg:
                return True
        elif curr.item > arg:
                return self.rec_is_present(arg,curr.left)
        else:
                return self.rec_is_present(arg,curr.right)  