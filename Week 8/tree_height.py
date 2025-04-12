'''
Example Input Tree #1

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 3

Example Input Tree #2 

      4 

Input: root = 4
Expected Output: 1
'''

'''
PLAN:
Traverse each side while maintaining a counter with current height
Get max height of left and right subtree and add that that to current height
'''

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def height(root):
	return height_helper(0, root)

#unchanged traverse from last problem
def height_helper(counter, node):
    if node is None:
         return counter
    
    return max(height_helper(counter+1, node.left), height_helper(counter+1, node.right))


root = TreeNode(4, 
   TreeNode(2, TreeNode(1), TreeNode(3)),
   TreeNode(5, None, None))

print(height(root))

root = TreeNode(4,None, None)

print(height(root))