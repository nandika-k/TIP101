'''
Problem 2: Root-to-Leaf Paths
Given the root of a binary tree, return a list of all root-to-leaf paths in any order.

A leaf is a node with no children.

Evaluate the time complexity of your function.


Example Usage:

Example Input Tree #1:

  1
 / \
2   3
 \  
  5         

Example Input: root = 1
Expected Output: ["1->2->5", "1->3"]
["1->3", "1->2->5"] is also valid

Example Input Tree #2:
  1    

Example Input: root = 1
Expected Output: ["1"]


understand:
- root == null return 0
- root has no right or left return root 

match
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_path_helper(root, str_tree):
    if root is None:
        return str_tree
    if root.left is None and root.right is None:
        str_tree += str(root.val)
        return str_tree
    
    str_tree += str(root.val) + "->"

    return tree_path_helper(root.left, str_tree) and tree_path_helper(root.right, str_tree)
    

def binary_tree_paths(root):
    
    arr_bin = []
    arr_bin.append(tree_path_helper(root.left, str(root.val) + "->"))
    arr_bin.append(tree_path_helper(root.right, str(root.val) + "->"))


    # str_left = root.val +"->"+ str_left 
    return arr_bin


left1 = TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(4, None, None), None))
right1 = TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None, ))
root = TreeNode(1, left1, right1)
print(binary_tree_paths(root))


# add me on www.linkedin.com/in/kadin-suga