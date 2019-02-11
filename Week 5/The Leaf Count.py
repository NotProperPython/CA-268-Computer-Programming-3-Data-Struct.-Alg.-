#
#   Complete the recursive_count method shown below which will count all the elements in the tree
#
#   Remember what it has to do. The method needs to count the current element as well as all the
# elements of its left subtree and all the elements of its right subtree.
#
#   It can be accomplished in one return statement.
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

    def recursive_count(self, curr):
        if curr == None:
            return 0
        if (curr.left == None) and (curr.right == None):# Base Case
            return 1
        else:
            return 0+(self.recursive_count(curr.left)+self.recursive_count(curr.right))


    def count_leaves(self):
        return self.recursive_count(self.root)