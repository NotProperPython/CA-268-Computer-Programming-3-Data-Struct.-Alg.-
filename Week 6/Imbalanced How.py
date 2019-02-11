def rotation_type(bst,ptr='abc'):
    if ptr =='abc':
        ptr = bst.root
        
    if ptr.left != None or ptr.right != None:
        if ptr.left != None:
            return 'l' + rotation_type(bst, ptr.left)
            
        else:
            return 'r' + rotation_type(bst, ptr.right)
    
    return '' 