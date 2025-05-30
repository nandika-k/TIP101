"""
Write a function above_threshold that takes in a list of integers lst
and an integer threshold as parameters. The function iterates through
the original list and returns a new list containing only numbers that
are greater than threshold.
"""

# Input: lst = [8,2,13,11,4,10,14] threshold = 10
# Output: [13, 11, 14]

"""
Output is a new list

EDGE CASE
 - empty list
 - only one item
 - threshold is smaller than all items
 - no elements above threshold
 - duplicates
 - non-int items

Ask interviewer about these edge cases...
- Non-int items won't be passed.
- Is the list sorted? No
- Include duplicates in final list? 
"""

"""
PLAN:
Make a new list that I'll return
Use while or for loop to iterate through input lst
    Use a conditional to check whether current item is > than threshold
    Add current item to new list
Return list
"""

def above_threshold(lst, threshold):
    output = []

    for num in lst:
        if num > threshold:
            output.append(num)
    return output

print(above_threshold([8,2,13,11,4,10,14], 10))
print(above_threshold([], 0))