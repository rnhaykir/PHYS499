from BinaryTree import BinaryTree, TreeNode

def swap(root):
    
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left
    
    swap(root.left)
    swap(root.right)
    
    return root

def tree_to_tuple(node):
    if node is None:
            return None
    return (node.element, tree_to_tuple(node.left), tree_to_tuple(node.right))