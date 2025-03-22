# Understand: We're converting a Python list into a linked list. 
# Match: Using linked list 
# Plan: Converting list to linked list 
# Take list at indice: 
    # Store the value into a new node 
    # Point to next node in list
    # Convert that indice intno a new neode

def print_ll(head):
	if head is None: # no elements
		return None
	
	if head.next is None: # only one element
	    print(head.value)
		
	temp = head
	while temp.next != None:
		print(f"{temp.value} -> ", end="")
		temp = temp.next
	print(temp.value)  # Off-by-one
	
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def convert(lst):
	if len(lst) == 0:
		return None
	
	head = Node(lst[0])
	current = head
	
	for i in range(1, len(lst)):
		current.next = Node(lst[i])
		current = current.next
	
	return head

def add_first(head, new_node):
	if head is None:
		return new_node
	new_node.next = head 
	return new_node

def get_tail(head):
	if head is None:
		return None
	current = head
	while (current.next is not None):
	    current = current.next
		
	return current.value

def ll_replace(head, original, replacement):
	if head is None:
		return None
	
	current = head
	while current is not None:
		if (original == current.value):
			current.value = replacement
		current = current.next
	return head

def listify_first_n(head, n):
	lst = []
	current = head
	for i in range(n):
		if current is None:
			break 
		lst.append(current.value)
		current = current.next
		
	return lst

def ll_insert(head, val, i):
	current = head
	prev = None
	for j in range(i+1):
		if current is None:
			break 
		if (i == j): 
			new_node = Node(val, current)
			prev.next = new_node
		current = current.next
		prev = current

# linked list: 3 -> 8 -> 12 -> 9
head = convert([3, 8, 12, 9])
ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9
print_ll(head)


empty = []
lst=['Jigglypuff','Wigglytuff','Ditto']
node_1 = convert(lst)
node_2 = node_1.next
print_ll(node_1)
print_ll(convert(empty))

new_node = Node('Eevee')
add_first(node_1, new_node)
add_first(convert(empty), new_node)
#print_ll(new_node)
#print_ll(new_node)
print(get_tail(new_node))
# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
print(ll_replace(head, 5, "banana"))

print_ll(head)

lst = listify_first_n(node_1,2)
print(lst)

# linked list: j -> k -> l 
lst2 = listify_first_n(convert(['j','k', 'l']),5)
print(lst2)
	
ll_insert(head, 20, 2)
