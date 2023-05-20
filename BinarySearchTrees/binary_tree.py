class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def parse_tuple(data):
        """
        Parses a tuple representing a binary tree and returns its root node.

        :param data: The tuple representing the binary tree.
        :return: The root node of the binary tree.
        """
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node

    def display_keys(node, space='\t', level=0):
        """Recursively prints the keys of a binary tree in a top-down fashion.

        Args:
        - node: The root node of the binary tree.
        - space: A string representing the spacing between levels of the tree (default: '\t').
        - level: An integer representing the level of the node in the binary tree (default: 0).
        """

        # If the node is empty
        if node is None:
            print(space*level + 'x')
            return   
        
        # If the node is a leaf 
        if node.left is None and node.right is None:
            print(space*level + str(node.key))
            return
        
        # If the node has children
        TreeNode.display_keys(node.right, space, level+1)
        print(space*level + str(node.key))
        TreeNode.display_keys(node.left,space, level+1)

    def tree_inorder_traversal(node):
        """Traverse the binary tree in inorder and return the keys of the nodes in a list."""
        if node is None:
            return []
        return(TreeNode.tree_inorder_traversal(node.left) + [node.key] + TreeNode.tree_inorder_traversal(node.right))
    
    #Traverse the binary tree in preorder and return the keys of the nodes in a list.
    def tree_preorder_traversal(node):
        """Traverse the binary tree in preorder and return the keys of the nodes in a list."""
        if node is None:
            return []
        return([node.key] + TreeNode.tree_preorder_traversal(node.left) + TreeNode.tree_preorder_traversal(node.right))
    
    #Traverse the binary tree in postorder and return the keys of the nodes in a list.
    def tree_postorder_traversal(node):
        """Traverse the binary tree in postorder and return the keys of the nodes in a list."""
        if node is None:
            return []
        return(TreeNode.tree_postorder_traversal(node.left) + TreeNode.tree_postorder_traversal(node.right) + [node.key])