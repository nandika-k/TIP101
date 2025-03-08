from collections import Counter

"""
UNDERSTAND
 - care about unintended repeating characters
 - if a character is missing, it's automatically false
 - extra letter at the end is not long pressed, order matters

PLAN
 - if name and typed are the same, return True
 - use count() in a for loop to check whether each char is present at least the same number of times
 - declare two pointers, one for name and one for typed
 - declare prev var to store the char before the one the pointer is at for typed
 - while loop until p1 < len(name) or p2 < len(typed)
"""

def is_long_pressed(name, typed):
    if name == typed:
        return True

    for letter in name:
        if name.count(letter) > typed.count(letter):
            return False
    
    p1 = p2 = 1
    prev = typed[0]

    while p1 < len(name) and p2 < len(typed): #is it and or or
        if name[p1] != typed[p2] and typed[p2] == prev:
            return True
        p1 += 1
        p2 += 1

    return False



name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))