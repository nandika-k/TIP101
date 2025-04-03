def countdown(n):
	if n > 0:
		print(n)
		countdown(n - 1)
		
def countdown_iterative(n):
	while n > 0: 
		print(n)
		n -= 1
		
# Understand: Write recursive fibonacci sequence function
# Plan: If n == 0, return 0, if n == 1, return 1 
# Return fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
	if n == 0 or n == 1:
		return n
	return fibonacci(n-1)+fibonacci(n-2)

# Understand: returning the product of all integers in a list 
# Match: recursion, list slicing
# Plan: 
# first element of the list * second of list 
# shrink the list on every recursive call until the lenghth of the list is 1
# first call: [0] * [1:] (1 *2) [1,2,3,4,5]
#  second call: [0] * [1:] (2 * 3) [2,3,4,5]
# result: 5


def list_product(lst):
	if len(lst) == 1:
		return lst[0]
	return lst[0] * list_product(lst[1:])

# Understand: Check to see if a number is a power of 4 
# Match: recursion 
# Plan: 
# Keep dividing until we hit 1
# Base case: is n == 1? 
def is_power_of_four(n):
	if n == 1:
		return True
	elif n % 4 == 0:
		return is_power_of_four(n/4) 
	else:
		return False
		

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found within bounds

		# find middle index of list
    mid = (left + right) // 2
    
    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # If the target is greater than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Plan: lst = [1, 3, 5, 7, 9, 11, 13, 15],
# list: [1, 3, 5, 7, 9,] 
# if smaller [: mid]
# if bigger [mid+1:]
# List of size n:
# Take n // 2 = mid 
# Give you list[mid]
def binary_search_iterative(arr, target):
	if not arr:
		return -1
	if len(arr) == 1 and target != arr[0]:
		return -1
	elif len(arr) == 1 and target == arr[0]:
		return 0
	
	left = 0
	right = len(arr) - 1
	mid = (left + right) // 2

	while left < right:
		if (target == arr[mid]):
			return mid
		elif target < arr[mid]:
			right = mid - 1
			mid = (left + right) // 2
		else: 
			left = mid + 1
			mid = (left + right) // 2
		
	return -1 
# countdown(5)
# countdown_iterative(5)

#print("Fibonacci sequence: ", fibonacci(6))

#print(list_product([1, 2, 3, 4, 5]))

#print(is_power_of_four(64))
#print(is_power_of_four(63))

lst = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search_iterative(lst, 11))