"""
EDGE CASES:
 - Empty list

PLAN
Use a for loop to iterate through list
    If match found
        return true
Return false 
"""


def check_num(lst, num):
    for item in lst:
        if item == num:
            return True
    return False

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1, "\n", flag2)