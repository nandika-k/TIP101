"""
PLAN
Create new list output
Iterate through lst
    Add 1 to each item and store in output
Return output
"""


def increment_values(lst):
    output=[]
    for num in lst:
        output.append(num+1)
    return output

print(increment_values([3,5,8,2]))