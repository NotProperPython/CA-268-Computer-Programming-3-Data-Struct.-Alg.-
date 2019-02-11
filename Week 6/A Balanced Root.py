def is_avl(bst):
    # Determine whether this bst is AVL balanced or not.
    if bst == None:
        return True
        
    if abs(bst.r_height(bst.root.right) - bst.r_height(bst.root.left)) > 1:
        return False
        
    return True 