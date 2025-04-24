"""
Problem 1: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
def is_valid(s):
    stack = []

    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif char == "}":
            if len(stack) == 0 or stack.pop() != '{':
                return False
        elif char == "]":
            if len(stack) == 0 or stack.pop() != '[':
                return False
    return len(stack) == 0


s = "()[{}"
print(is_valid(s))
        
s = "[(){}]"
print(is_valid(s))