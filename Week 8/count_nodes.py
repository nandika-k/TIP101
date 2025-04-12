class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def count_nodes(head, val):
    count = 0
    curr = head
    prev = None

    while curr is not None:
        if curr.value == val:
            count += 1
        curr = curr.next

    return head

def del_nodes(head, val):
    curr = head
    prev = None
    temp_head = head

    while curr is not None:
        if curr.value == val:
            if prev is None:
                temp_head = curr.next
            else:
                prev.next = curr.next
        prev = curr
        curr = curr.next
        

    return temp_head

def print_list(head):
    curr = head

    while curr is not None:
        print(curr.value)
        curr = curr.next

five = Node(3)
four = Node(3, five)
three = Node(3, four)
two = Node(3, three)
one = Node(3, two)
zero = Node(3, one)

print_list(del_nodes(None,3))