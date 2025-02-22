"""
PLAN
- Does python have a reverse function for lists?

"""

def reverse_list(lst):
    lst.reverse()
    return lst

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)

lst = [5,4,8]
rev_lst = reverse_list(lst)
print(rev_lst)