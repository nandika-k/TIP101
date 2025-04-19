from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list
    if root is None:
        return []

    # Create an empty queue using deque
    queue = deque([])
    # Create an empty list to store the explored nodes
    explored = []

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes
    while len(queue) != 0:
        node = queue.popleft()
        explored.append(node.val)

        # Add each of the popped node's children to the end of the queue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    # Return the list of visited nodes
    return explored

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_order(root))