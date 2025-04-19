'''
If the tree is empty:
    return an empty list

Create an empty queue
Create an empty list to store visited nodes

Add the root into the queue

While the queue is not empty:
    Pop the next node off the queue 
    Add the popped node to the list of visited nodes

    Add the popped node's left child to the queue
    Add the popped node's right child to the queue

PLAN:

'''
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
        
def min_depth(root):
    #depth counter
    depth = 0

	# If the tree is empty:
    # return an empty list
    if root is None:
        return depth

    # Create an empty queue using deque
    queue = deque([])
    # Create an empty list to store the explored nodes
    explored = []

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes
    curr_depth = 0
    while len(queue) != 0:
        node = queue.popleft()
        explored.append(node)

        # Add each of the popped node's children to the end of the queue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

        if node.right in explored and node.left in explored:
            curr_depth += 1

        if node.right is None and node.left is None:
            if depth == 0:
                depth = curr_depth
            else:
                depth = min(depth, curr_depth)
        if node is explored[0]:
            curr_depth = 0
        
    # Return the list of visited nodes
    return depth

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Example 1:", min_depth(root))
root =TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5,TreeNode(6)))))
print("Example 2:", min_depth(root))
