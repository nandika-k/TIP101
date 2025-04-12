'''
Given a string s, find the first non-repeating character in it and treturn its index. If 
it doesn't exist, return -1.

input_a = "leetcode" # output is 0
input_b = "loveleetcode" # output is 2
input_c = "aabb" # output is -1

Don't worry about malformed, empty, etc strings

PLAN:
index = 0 to track index of current letter
found = false, becomes true when a non-repeating char is found
for letter in string:
    if the count of the letter is 1
        found = true
    if found
        return index
    increase index every iteration
if not found, return -1
else return index
'''

def first_unique(s):
    index = 0
    found = False

    for letter in s:
        if s.count(letter) == 1:
            found = True
            return index
        index += 1

    if not found:
        return -1
    else:
        return index

input_a = "leetcode" # output is 0
input_b = "loveleetcode" # output is 2
input_c = "aabb" # output is -1

print(input_a, first_unique(input_a))
print(input_b, first_unique(input_b))
print(input_c, first_unique(input_c))