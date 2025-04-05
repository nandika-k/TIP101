"""
UNDERSTAND:
Use binary search on sorted list of 0s and 1s
Determine number of 1s in sorted list (in O(log n) time)

PLAN:
Check the middle of lst
    if it's a 1
        call count_ones with first half of the list
	if it's a 0
        call count_ones with the second half of the list
"""

def count_ones(lst):
    left,right=0,len(lst)-1
    index = len(lst)
	
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == 1:
            right = middle-1
            index = middle
        else:
            left = middle+1

    return len(lst) - index
                
print(count_ones([0, 0, 0, 1, 1, 1]))  
print(count_ones([0, 0, 0, 0, 0]))    
print(count_ones([1, 1, 1, 1]))       
print(count_ones([0, 1]))              
print(count_ones([1]))