class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
#Create root node
root = TreeNode(10)

#Creating children nodes
root.left = TreeNode(5)
root.right = TreeNode(15)
