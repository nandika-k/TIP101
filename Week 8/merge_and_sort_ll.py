'''
You are given the heads of two linked lists, list1 and list2

Merge them into one sorted list. It should be made by splicing together nodes of the first two lists.

Return the head of the merged linked list.

PLAN:
Create two pointer nodes to iterate through both sorted lists
Create a new head pointer for the merged list
Create a current pointer (curr) for the merged list that will always point to the last added node

Compare the values of the current node, check that the pointers are not null
    If the head node is Null, set the head node to the lower value node
    else, set curr.next to the lower value node

    Advance the pointer for the list that the node came from

if one of the pointers is null, add all the elements of the other list in order to curr.next

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

listA = ListNode(2, next=ListNode(5, next=ListNode(10)))
listB = ListNode(4, next=ListNode(6, next=ListNode(7)))

def mergeTwoLists(list1, list2):
    node1 = list1
    node2 = list2
    
    merged_head = None
    curr = None
   
    while node1 is not None and node2 is not None:
        node_to_append = None
        if node1.val > node2.val:
            node_to_append = node2
            node2 = node2.next
        else:
            node_to_append = node1
            node1 = node1.next

        if merged_head is None:
           merged_head = node_to_append
           curr = merged_head
        else:
            curr.next = node_to_append
            curr = curr.next

    if node1 is None:
        curr.next = node2
    else:
        curr.next = node1
    
    return merged_head

def print_linked_list(head):
    curr = head

    while curr is not None:
        print(curr.val)
        curr = curr.next
   
print_linked_list(mergeTwoLists(listA, listB))