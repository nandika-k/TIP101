class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def count_nodes(head, val):
    count = 0
    curr = head
    
    while curr is not None:
        if curr.value == val:
            count += 1
        curr = curr.next

    return count

