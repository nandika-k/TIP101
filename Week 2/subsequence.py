"""
PLAN
for loop to iterate through seq
    for loop to iterate through lst
        if lst_num = seq_num
            break
        
"""

def is_subsequence(lst, sequence):
    counter = 0
    for s in sequence:
        for num in lst:
            if s == num:
                   counter += 1
                   break
    
    return counter == len(sequence)
             

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

lst = [5, 1, 22, 25, 6, -1, 8]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))