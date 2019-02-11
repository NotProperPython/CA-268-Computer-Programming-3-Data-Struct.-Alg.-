from Node import Node

#
#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def add(tree, item):
    if tree.root == None:
        tree.root = Node(item, None, None)
        return None
    else:
        ancestors = []
        child_tree = tree.root
        while child_tree != None:
            parent = child_tree
            ancestors.append(parent)
            if item < child_tree.item:
                child_tree = child_tree.left
            elif item > child_tree.item:
                child_tree = child_tree.right
        if item < parent.item:
            parent.left = Node(item, None, None)
        elif item > parent.item:
            parent.right = Node(item, None, None)
        for ancestor in ancestors[-2::-1]:
            if abs(tree.recurse_height(ancestor.left) - tree.recurse_height(ancestor.right)) > 1:
                return ancestor.item
        # Ignore the case where the item is equal.
        #
        #   Note that you can get the height of a node by calling tree.recurse_height().
        #       For example, the height of the root is tree.recurse_height(tree.root)