'''
Example Input Tree #1

      1
     / \
    /   \
   1     1
  / \     \
 1   1     1

Input: root = 1
Expected Output: True

Example Input Tree #2

      1
     / \
    /   \
   1     2
  / \     \
 1   1     1

Input: root = 1
Expected Output: False
'''

'''
PLAN:
Store the overall root value
Traverse tree (pre-order) using a helper method that takes in overall root node's value and a node
    compare each node's value
    if node's value is not the same as the root value, return False
return True after traversing the whole tree

traverse_and_check plam
if node is none, just return

if node.val != val, return false

traverse_and_check(left)
traverse_and_check(right)
'''
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
    value = root.val
    return traverse_and_check(value, root)   

def traverse_and_check(val, node):
    if node is None:
        return True

    if node.val != val:
        return False

    if node.left == None and node.right == None:
        return True

    return traverse_and_check(val, node.left) and traverse_and_check(val, node.right)

#example 1
root = TreeNode(1, 
   TreeNode(1, TreeNode(1), TreeNode(1)),
   TreeNode(1, None, TreeNode(1) ))
print(is_univalued(root))

#example 2
root2 = TreeNode(1, 
   TreeNode(1, TreeNode(1), TreeNode(1)),
   TreeNode(2, None, TreeNode(1) ))
print(is_univalued(root2))

