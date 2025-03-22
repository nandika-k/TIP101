class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = None
    def print_list(self):
        node = self
        while node != None:
            print(node.value, end=" ")
            node = node.next
"""
Check if head == None, return None
And if head.next == None, return head
Else
    While var_next.next != None
        Set up a curr_head pointer
        Set up two pointers one for the curr node, one for the var_next node (in the original list)
        Assign the curr node's next to the var_next node's next
        Set curr_head = var_next
        Assign the var_next node's next to the curr node
        Move the var_next node pointer to the curr node's next or the third node
        Set curr node's next to the var_next node
"""
def reverse_linked_list(head):
    curr = head
    prev = None

    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        if next_node != None:
            curr = next_node.next

# Creating the linked list
node_five = Node(5)
node_four = Node(4, node_five)
node_three = Node(3, node_four)
node_two = Node(2, node_three)
head = Node(1, node_two)

# Printing original list
print("Original List:")
head.print_list()

# Reversing and printing the list
reversed_head = reverse_linked_list(head)
print("Reversed List:")
reversed_head.print_list()