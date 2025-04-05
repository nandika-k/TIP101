"""
UNDERSTAND:
If there are no parenthesis or all are paired, return true

PLAN:
if len(odd)
	return false
	if empty string
		return true
	if str[0] is '(' and str[last char] is ')'
		is_nested(str[1:last char-1])
return False

"""

def is_nested(paren_s):
	if len(paren_s) % 2 == 0:
		if len(paren_s) == 0:
			return True
		
		length = len(paren_s)
		if paren_s[0] == '(' and paren_s[length-1] == ')':
			#may not be the most efficient in terms of space
			return is_nested(paren_s[1:length-1])
	return False

		
print(is_nested("(())"))
print(is_nested("(()")) 