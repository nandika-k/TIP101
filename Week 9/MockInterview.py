'''
Given the root of a binary tree and an integer target_sum, return True if the
tree has a root-to-leaf path such that adding up all the values along the path
equals target_sum. A leaf is a node with no children.

UNDERSTAND:
Edge Cases: root is the only node or is Null, multiple possible answers (go with first one found)

PLAN:
def sum_path
Base Case: node is null
    return
Base Case: leaf node
    sum += value of node

    if sum equals target sum:
        return True
Other Cases:
    return def_sum(node.right, sum+node.val, target_sum) or def_sum(node.left, sum+node.val, target_sum)

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_path(node, sum, target_sum):
    if node is None:
        return sum == target_sum
    if node.right is None and node.left is None:
        sum += node.val
        return sum == target_sum
    else:
        return sum_path(node.right, sum+node.val, target_sum) or sum_path(node.left, sum+node.val, target_sum)

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(sum_path(None, 0, 22))

# Examples

#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
#  / \      \
# 7   2      1
# target_sum = 22
# Output: True

#     1
#    / \
#   2   3

# target_sum = 5
# Output: False


#      1

# target_sum = 1
# Output: True

#Other problem and groupmate's code
def invert(root):
    if root is None:
        return
    
    root.left, root.right = root.right, root.left

    invert(root.left)
    invert(root.right)

    return root