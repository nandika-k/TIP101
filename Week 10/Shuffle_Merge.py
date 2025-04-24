def shuffle_merge(head_a, head_b):
    list_a = head_a  
    list_b = head_b
    combined = head_a 
    head = None
    add_a = True
        
    while list_a and list_b: 
        if add_a:
            combined.next = list_a
            list_a = list_a.next
            add_a = False
        else:
            combined.next = list_b
            list_b = list_b.next
            add_a = True
        if not head:
            head= combined
    if not list_a and list_b is not None:
        combined.next = list_b
    if not list_b and list_a is not None:
        combined.next = list_a
    
    return head