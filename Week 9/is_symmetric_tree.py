'''
Problem 1: Is Symmetric Tree
Given the root of a binary tree, return True if the tree’s 
left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). 
Return False otherwise.

Evaluate the time complexity of your function.


Example Tree #1:

       1
     /   \
    /     \
   2       2
  / \     / \
 3   4   4   3
           
 

Input: root = 1
Expected Output: True


Example Tree #2:

        1
      /   \
     /     \
    2       2
     \       \
      3       3
         

Input: root = 1
Expected Output: False


Understand:
- Is none
- Extra child

Match
- In order traversal

Plan:
- Send the left of the root and right of the root to a helper method
    - In helper method store all values into an array
        - ...
    - return array
- Compare left and right
    - if equal return true
        else
            false

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sym_helper(root, isLeft, root_arr):
    if root is None:
        return root_arr
    
    if isLeft:
        root_arr.append(root.val)
        return sym_helper(root.left, isLeft, root_arr) and sym_helper(root.right, isLeft, root_arr)
    else:
        root_arr.append(root.val)
        return sym_helper(root.right, isLeft, root_arr) and sym_helper(root.left, isLeft, root_arr)

    
         

def is_symmetric(root):
    left_arr = []
    right_arr = []
    
    if root:
        left_arr = sym_helper(root.left, True, left_arr)
        right_arr = sym_helper(root.right, False, right_arr)

        if left_arr == right_arr:
            return True
        else:
            return False
    return False

'''
Example Tree #1:

       1
     /   \
    /     \
   2       2
  / \     / \
 3   4   4   3
'''

left1 = TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(4, None, None), None))
right1 = TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None))
root = TreeNode(1, left1, right1)

print(is_symmetric(None))
