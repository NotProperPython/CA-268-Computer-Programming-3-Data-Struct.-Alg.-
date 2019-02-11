#
#       complete the count method below
#
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
        # This is a non recursive add method.
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
            elif item > parent.item:
                parent.right = Node(item, None, None)
            #else:
            #   equal ... don't add it to the set.

    def recursive_range(self, lo, hi, ptr, count=0):
        if ptr == None:
            return 0
        elif lo <= ptr.item <= hi:
            return 1 + (self.recursive_range(lo, hi, ptr.left, count) + self.recursive_range(lo, hi, ptr.right, count))
        elif ptr.item > lo:
            return self.recursive_range(lo, hi, ptr.left, count)
        elif ptr.item < hi:
            return self.recursive_range(lo, hi, ptr.right, count)

    def count(self, lo, hi):
        return self.recursive_range(lo, hi, self.root)